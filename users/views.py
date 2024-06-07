from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from .serializers import *
from .models import *


class RegisterView(APIView):
    @swagger_auto_schema(
        request_body=UserPostSerializer
    )
    def post(self, request):
        serializer = UserPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(role='regular')
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserDetailsView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        return Response(status=401)


class UserUpdateView(APIView):
    @swagger_auto_schema(
        request_body=UserSerializer
    )
    def put(self, request):
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        return Response(status=401)


class UserDeleteView(APIView):
    def delete(self, request):
        if request.user.is_authenticated:
            user = request.user
            user.delete()
            return Response(status=204)
        return Response(status=401)


class FollowCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        request_body=FollowSerializer
    )
    def post(self, request):
        try:
            serializer = FollowSerializer(data=request.data)
            if request.user.id == int(request.data.get("to_user")):
                return Response("User cannot follow himself!", status=400)
            if serializer.is_valid():
                serializer.save(from_user=request.user)

                to_user = User.objects.get(id=serializer.data['to_user'])
                to_user.followers_count = len(Follow.objects.filter(to_user=to_user))
                to_user.save()

                from_user = request.user
                from_user.following_count = len(Follow.objects.filter(from_user=from_user))
                from_user.save()

                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response(str(e), status=400)


class FollowRemoveView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, user_id):
        if request.user.is_authenticated:
            from_user = get_object_or_404(User, id=user_id)
            to_user = request.user

            follow = get_object_or_404(Follow, from_user__id=user_id, to_user=request.user)
            follow.delete()

            from_user.following_count = len(Follow.objects.filter(from_user=from_user))
            from_user.save()

            to_user.followers_count = len(Follow.objects.filter(to_user=to_user))
            to_user.save()
            return Response('Successful!', status=204)
        return Response(status=401)


class UnFollowView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, user_id):
        if request.user.is_authenticated:
            from_user = request.user
            to_user = get_object_or_404(User, id=user_id)

            follow = get_object_or_404(Follow, from_user=request.user, to_user__id=user_id)
            follow.delete()

            from_user.following_count = len(Follow.objects.filter(from_user=from_user))
            from_user.save()

            to_user.followers_count = len(Follow.objects.filter(to_user=to_user))
            to_user.save()
            return Response("Successful!", status=204)
        return Response(status=401)
