from rest_framework.serializers import ModelSerializer
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'password', 'role', 'first_name', 'last_name', 'email', 'phone_number',
            'bio', 'followers_count', 'following_count', 'likes_count', 'date_joined', 'is_superuser'
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'followers_count': {'read_only': True},
            'following_count': {'read_only': True},
            'likes_count': {'read_only': True},
            'date_joined': {'read_only': True},
            'is_superuser': {'read_only': True},
            'role': {'read_only': True},
        }

    def to_representation(self, instance):
        user = super(UserSerializer, self).to_representation(instance)
        images = UserImage.objects.filter(user__id=user['id'])
        images_serializer = UserImageSerializer(images, many=True)
        user.update(
            {
                'images': images_serializer.data
            }
        )
        return user


class UserPostSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'phone_number', 'bio')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserImageSerializer(ModelSerializer):
    class Meta:
        model = UserImage
        fields = '__all__'


class FollowSerializer(ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'

        extra_kwargs = {
            'from_user': {'read_only': True},
        }
