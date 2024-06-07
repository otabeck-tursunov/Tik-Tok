from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class VideosView(APIView):
    def get(self, request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
