
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from tag.models import Tag
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from recipes.models import Recipe
from ..permission import IsOwner
from ..serializers import RecipeSerializer, TagSerializer, RecipeSerializer2


class RecipeAPIv3Pagination(PageNumberPagination):
    page_size = 2


class RecipeAPIv4List(ModelViewSet):
    queryset = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIv3Pagination
    # permission_classes = [IsOwner, ]
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    #Fala quais métodos são permitidos
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']

    def get_queryset(self):
        #Se não digitado nada, será retornado o mesmo que está na variavel queryset
        qs = super().get_queryset()
        
        #Vai tentar pegar o category ID da url:
        # exemplo: 
        category_id = self.request.query_params.get('category_id', None)

        if category_id is not None:
            qs = qs.filter(category_id=category_id)

        return qs

    def get_object(self):
        pk = self.kwargs.get('pk')
        
        obj = get_object_or_404(
                self.get_queryset(),
                pk=pk
            )

        #Verifica no permissions.py o método has_object_permission
        self.check_object_permissions(self.request, obj)

        return obj

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsOwner(), ]
        
        return super().get_permissions()

    def partial_update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        recipe = self.get_object()
        serializer = RecipeSerializer(
            instance=recipe,
            data=request.data,
            many=False,
            context={'request': request},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class RecipeAPIv3List(ListCreateAPIView):
    queryset = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIv3Pagination


#Cria um ponto para deletar um registro
class RecipeAPIv3Detail(RetrieveDestroyAPIView):
    #Faz a busca dos itens
    queryset = Recipe.objects.get_published()

    #Serializa os dados encontrados na queryset
    serializer_class = RecipeSerializer

    #Define o numero de registro por página
    pagination_class = RecipeAPIv3Pagination

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        recipe = self.get_queryset().filter(pk=pk).first()
        serializer = RecipeSerializer(
            instance=recipe,
            data=request.data,
            many=False,
            context={'request': request},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
        )


class RecipeAPIv2List(APIView):
    def get(self, request):
        print('AQUI!!')
        recipes = Recipe.objects.get_published()[:10]
        serializer = RecipeSerializer(
            instance=recipes,
            many=True,
            context={'request': request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class RecipeAPIv2Detail(APIView):
    def get_recipe(self, pk):
        recipe = get_object_or_404(
            Recipe.objects.get_published(),
            pk=pk
        )
        return recipe

    def get(self, request, pk):
        recipe = self.get_recipe(pk)
        serializer = RecipeSerializer(
            instance=recipe,
            many=False,
            context={'request': request},
        )
        return Response(serializer.data)

    def patch(self, request, pk):
        recipe = self.get_recipe(pk)
        serializer = RecipeSerializer(
            instance=recipe,
            data=request.data,
            many=False,
            context={'request': request},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
        )

    def delete(self, request, pk):
        recipe = self.get_recipe(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Avisa que é uma request do django rest
@api_view(http_method_names=['get', 'post'])
def recipe_api_list(request):
    if request.method == 'GET':
        recipes = Recipe.objects.get_published()[:10]
        #O serializer espera sempre um objeto, quando indicado o many mostra para o serializer que será uma lista o resultado.
        serializer = RecipeSerializer(instance=recipes, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        #Serializer pode ser usado para ler e para gravar
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data(), 
                            status=status.HTTP_201_CREATED
                            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view()
def recipe_api_detail(request, pk):
    recipe = get_object_or_404(
        Recipe.objects.get_published(),
        pk=pk
    )
    serializer = RecipeSerializer(instance=recipe, many=False, context={'request': request})

    return Response(serializer.data)
    # recipe = Recipe.objects.get_published().filter(pk=pk).first()

    # if recipe:
    #     serializer = RecipeSerializer(instance=recipe, many=False)
    #     return Response(serializer.data)
    # else:
    #     return Response({'Detail': 'Eita'}, status=status.HTTP_418_IM_A_TEAPOT)

@api_view()
def recipe_api_detail2(request, pk):
    recipe = get_object_or_404(
        Recipe.objects.get_published(),
        pk=pk
    )
    serializer = RecipeSerializer2(instance=recipe, many=False, context={'request': request})

    return Response(serializer.data)
    # recipe = Recipe.objects.get_published().filter(pk=pk).first()

    # if recipe:
    #     serializer = RecipeSerializer(instance=recipe, many=False)
    #     return Response(serializer.data)
    # else:
    #     return Response({'Detail': 'Eita'}, status=status.HTTP_418_IM_A_TEAPOT)

@api_view()
def recipe_api_tag_detail(request, pk):
    
    tag = get_object_or_404(
        Tag.objects.all(),
        pk=pk
    )
    
    serializer = TagSerializer(
        instance=tag, 
        many=False,
        context={'request': request}
        )

 
    return Response(serializer.data)
    