# serializer means to convert from complicated data to simple python datatype

from rest_framework import serializers

from .models import Article

# ModelSerializer
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']
