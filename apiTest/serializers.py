from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #fields = ['id', 'title', 'content', 'author', 'email']
        fields = '__all__'





"""
class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    content = serializers.CharField(max_length=6000)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date_published = serializers.DateTimeField()

    def create(self, validated_data):
        return Post.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('title', instance.content)
        instance.author = validated_data.get('title', instance.author)
        instance.email = validated_data.get('title', instance.email)
        instance.date_published = validated_data.get('title', instance.date_published)
        instance.save()
        return instance 
    """
