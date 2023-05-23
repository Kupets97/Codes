from rest_framework import serializers

from search_code.models import Code, Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Category.
    """
    class Meta:
        model = Category
        fields = ('name',)


class CodeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Code.
    """
    category = CategorySerializer()

    class Meta:
        model = Code
        fields = ('code', 'description', 'category')

    def to_representation(self, instance):
        """
        Возвращает dict с id и name категории вместо объекта.
        """
        representation = super().to_representation(instance)
        category_representation = representation.pop('category')
        representation['category'] = {
            'id': category_representation['id'],
            'name': category_representation['name']
        }
        return representation