"""
URL configuration for dx_movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter # 导入路由器
from movie import views
from account import views as account_views
from trade import views as trade_views

router = DefaultRouter() # 创建路由器
router.register(r'movie', views.MovieViewSet) # 注册路由
router.register(r'category', views.CategoryViewSet) # 注册目录路由
router.register(r'collects', account_views.CollectViewSet, basename='collect') # 注册收藏路由
router.register(r'cards', trade_views.CardViewSet, basename='card') # 注册会员卡路由
router.register(r'orders', trade_views.OrderViewSet, basename='order') # 注册订单路由

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/movie/', include('movie.urls', namespace='movie')),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.jwt')),
    path('api/alipay/', trade_views.AlipayAPIView.as_view()),
    path('api/callback/', trade_views.AlipayCallbackAPIView.as_view()),
    path('api/tasks/',trade_views.TaskAPIView.as_view()),
]