from rest_framework import serializers
from .models import Movie, Category

# # 定义序列化器
# class MovieListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Movie
#         fields = '__all__' # 序列化器字段
    
# class MovieDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = '__all__' # 序列化器字段
    
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__' # 序列化器字段

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' # 序列化器字段
