from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ImageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageContent
        fields = '__all__'

class VideoContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContent
        fields = '__all__'

class SubheadingContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubheadingContent
        fields = '__all__'

class ParagraphContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParagraphContent
        fields = '__all__'
        
class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many = True)
    images = ImageContentSerializer(many = True)
    videos = VideoContentSerializer(many = True)
    subheadings = SubheadingContentSerializer(many = True)
    paragraphs = ParagraphContentSerializer(many = True)

    class Meta:
        model = Article
        fields = '__all__'