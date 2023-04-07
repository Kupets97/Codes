from rest_framework import serializers

from search_code.models import Code, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class CodeSerialzier(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Code
        fields = ('code', 'description', 'category')

