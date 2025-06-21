from django.shortcuts import render
from django.http import JsonResponse, Http404

from .models import Movie, Category
from .serializers import MovieSerializer, CategorySerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
from utils.filters import MovieFilter


# Create your views here.

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     # 获取数据
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieListSerializer(movies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = MovieListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class MovieDetail(APIView):
#     def get(self, request, pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#             serializer = MovieDetailSerializer(movie)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Movie.DoesNotExist:
#             raise Http404("Movie does not exist")
    
#     def put(self, request, pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#             serializer = MovieDetailSerializer(movie, data=request.data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Movie.DoesNotExist:
#             raise Http404("Movie does not exist")
        
#     def delete(self, request, pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#             movie.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Movie.DoesNotExist:
#             raise Http404("Movie does not exist")

# class MovieList(generics.ListCreateAPIView):
#     queryset = Movie.objects.all() # 获取所有对象
#     serializer_class = MovieListSerializer # 序列化器

# class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all() # 获取所有对象
#     serializer_class = MovieDetailSerializer # 序列化器



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all() # 获取所有对象
    serializer_class = MovieSerializer # 序列化器
    filterset_class = MovieFilter # 过滤类
    permission_classes = [IsAdminOrReadOnly]
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


def TemplateView(request):
    return render(request, 'index.html')