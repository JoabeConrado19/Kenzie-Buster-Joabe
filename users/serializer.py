from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=127, write_only=True)
    is_superuser = serializers.BooleanField(read_only = True, default= False)
    email = serializers.CharField( max_length=127)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(default= None)
    is_employee = serializers.BooleanField(default= False)

    

    def validate(self, data):
        email = data.get('email')
        username = data.get('username')
        errors = {}
        if User.objects.filter(email=email).exists():
            errors['email'] = ['email already registered.']
        if User.objects.filter(username=username).exists():
            errors['username'] = ['username already taken.']
        if (errors):
            raise serializers.ValidationError(errors)
        return data

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
    
    def update(self, instance: User, validated_data: dict):

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.set_password(validated_data['password'])

        instance.save()

        return instance

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, write_only=True)
    password = serializers.CharField(max_length=127, write_only=True)
