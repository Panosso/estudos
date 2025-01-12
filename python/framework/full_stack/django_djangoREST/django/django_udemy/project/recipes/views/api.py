
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from tag.models import Tag

from recipes.models import Recipe
from ..serializers import RecipeSerializer, TagSerializer, RecipeSerializer2

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
    