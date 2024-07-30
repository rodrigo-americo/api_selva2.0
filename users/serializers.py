from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'userName', 'active', 'datecreatedAt']
        read_only_fields = ['id', 'active', 'datecreatedAt']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userName', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            userName=validated_data['userName'],
            password=validated_data['password']
        )
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['userName'] = user.userName
        return token
