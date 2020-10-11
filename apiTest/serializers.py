from rest_framework import serializers

from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    # category_name = serializers.CharField(source="get_category_name", read_only=True)
    category_name = serializers.ReadOnlyField(source="get_category_name")

    class Meta:
        model = Post
        fields = '__all__'

