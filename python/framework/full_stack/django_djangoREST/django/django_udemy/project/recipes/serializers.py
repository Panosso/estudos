from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Recipe
from tag.models import Tag
from authors.validators import AuthorRecipeValidator


#outro método de serializar
class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

class RecipeSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['id', 
                  'title',
                  'description',
                  'author',
                  'category',
                  'tags',
                  'public',
                  'preparation',
                  'tag_objects',
                  'tag_links',
                  ]

    #Com o source, eu aviso para o serializer qual o campo que ele tem que buscar
    public = serializers.BooleanField(source = 'is_published', read_only=True)
    
    #Esse SerializerMethodField procura um método com o nome get_(nome da variavel, nesse caso será o get_preparation)
    # ou posso criar um method com qulquer nome, porém tenho que informar como parametro
    preparation = serializers.SerializerMethodField(method_name='get_preparation', read_only=True)

    #Ele utiliza o nome category do model do recipe.
    category = serializers.StringRelatedField()

    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )

    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True
    )

    #Esse campo tagserializer só aceita o many=true por ser um campo de many to many
    tag_objects = TagSerializer(
        many=True, source='tags'
    )

    #Para qualquer PrimaryKeyRelatateField
    tag_links = serializers.HyperlinkedRelatedField(
        many = True,
        source = 'tags',
        read_only=True,
        view_name='recipes:recipes_api_v2_tag'
    )

    def get_preparation(self, recipe):
        return f'{recipe.preparation_time}'

    def validate(self, attrs):
        super_validate = super().validate(attrs)

        title = attrs.get('title')
        description = attrs.get('description')

        if title == description:
            raise serializers.ValidationError(
                {
                    "title": ["Posso", "ter", "mais de um erro"],
                    "description": ["Posso", "ter", "mais de um erro"],
                }
            )

        return super_validate

    def validate_title(self, value):
        title = value

        if len(title) < 5:
            raise serializers.ValidationError('Must have at least 5 chars.')

        return title

#Classe responsável com os campos que serão apresentados
# class RecipeSerializer(serializers.Serializer):

#     class Meta:
#         model = Recipe
#         fields = [
#             'id', 'title', 'description', 'author',
#             'category', 'tags', 'public', 'preparation',
#             'tag_objects', 'tag_links',
#             'preparation_time', 'preparation_time_unit', 'servings',
#             'servings_unit',
#             'preparation_steps', 'cover'
#         ]

#     #Com o source, eu aviso para o serializer qual o campo que ele tem que buscar
#     public = serializers.BooleanField(source = 'is_published', read_only=True)
    
#     #Esse SerializerMethodField procura um método com o nome get_(nome da variavel, nesse caso será o get_preparation)
#     # ou posso criar um method com qulquer nome, porém tenho que informar como parametro
#     preparation = serializers.SerializerMethodField(method_name='get_preparation', read_only=True)

#     #Ele utiliza o nome category do model do recipe.
#     category = serializers.StringRelatedField(
#         read_only=True,
#     )

#     author = serializers.PrimaryKeyRelatedField(
#         read_only=True
#     )

#     tags = serializers.PrimaryKeyRelatedField(
#         many=True, read_only=True
#     )

#     #Esse campo tagserializer só aceita o many=true por ser um campo de many to many
#     tag_objects = TagSerializer(
#         many=True, source='tags', read_only=True
#     )

#     #Para qualquer PrimaryKeyRelatateField
#     tag_links = serializers.HyperlinkedRelatedField(
#         many = True,
#         source = 'tags',
#         view_name='recipes:recipes_api_v2_tag',
#         read_only=True,
#     )

#     def get_preparation(self, recipe):
#         return f'{recipe.preparation_time}'
    
#     def validate(self, attrs):

#         if self.instance is not None and attrs.get('servings') is None:
#             attrs['servings'] = self.instance.servings

#         if self.instance is not None and attrs.get('preparation_time') is None:
#             attrs['preparation_time'] = self.instance.preparation_time

#         super_validate = super().validate(attrs)
#         AuthorRecipeValidator(
#             data=attrs,
#             ErrorClass=serializers.ValidationError,
#         )
#         return super_validate

#     def save(self, **kwargs):
#         return super().save(**kwargs)

#     def create(self, validated_data):
#         return super().create(validated_data)

#     def update(self, instance, validated_data):
#         return super().update(instance, validated_data)

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'author',
            'category', 'tags', 'public', 'preparation',
            'tag_objects', 'tag_links',
            'preparation_time', 'preparation_time_unit', 'servings',
            'servings_unit',
            'preparation_steps', 'cover'
        ]

    public = serializers.BooleanField(
        source='is_published',
        read_only=True,
    )
    preparation = serializers.SerializerMethodField(
        method_name='any_method_name',
        read_only=True,
    )
    category = serializers.StringRelatedField(
        read_only=True,
    )
    tag_objects = TagSerializer(
        many=True, source='tags',
        read_only=True,
    )
    tag_links = serializers.HyperlinkedRelatedField(
        many=True,
        source='tags',
        view_name='recipes:recipes_api_v2_tag',
        read_only=True,
    )

    def any_method_name(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'

    def validate(self, attrs):
        if self.instance is not None and attrs.get('servings') is None:
            attrs['servings'] = self.instance.servings

        if self.instance is not None and attrs.get('preparation_time') is None:
            attrs['preparation_time'] = self.instance.preparation_time

        super_validate = super().validate(attrs)
        AuthorRecipeValidator(
            data=attrs,
            ErrorClass=serializers.ValidationError,
        )

        return super_validate

    def save(self, **kwargs):
        return super().save(**kwargs)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)