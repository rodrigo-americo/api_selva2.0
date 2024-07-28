from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'userName', 'active', 'datecreatedAt']
        read_only_fields = ['id', 'active', 'datecreatedAt']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userName', 'password']

    def create(self, validated_data):
        user = User(
            userName=validated_data['userName']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
