from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import Profile

class CustomUniqueValidator(UniqueValidator):
    def __call__(self, value, serializer_field):
        self.message = '邮箱 %s 已存在' % value
        return super().__call__(value, serializer_field)

class CustomUserCreateSerializer(UserCreateSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[CustomUniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user =  UserCreateSerializer.create(self, validated_data)
        # 写入到profile表
        profile = Profile(user=user)
        profile.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

class CustomUserSerializer(UserSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta(UserSerializer.Meta):
        fields = (*UserSerializer.Meta.fields, 'profile')

