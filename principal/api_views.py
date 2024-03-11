from rest_framework import generics
from rest_framework.filters import SearchFilter
from django.contrib.auth import authenticate
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from os import *
from sys import *

from principal.models import Task, Annotation
from django.contrib.auth.models import User
from principal.serializers import UserSerializer, AnnotationSerializer, TaskSerializer

from principal.models import Annotation, Task
from django.shortcuts import get_object_or_404


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


# views.py
class ModelUserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = '__all__'

class ModelAnnotationListView(generics.ListAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    filter_backends = [SearchFilter]
    search_fields = '__all__'


class LoginView(APIView):
    permission_classes = ()

    def post(self, request, ):
        username = request.data['username']
        password = request.data['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'POST'])  # read, update, create
def _see_your_apis(request, *args, **kwargs):
    # permission_classes = [permissions.IsAuthenticated]
    # print(permission_classes)
    print('moi')
    qs = Annotation.objects.all().order_by('-deadline')
    serializer = AnnotationSerializer(qs, many=True)
    return Response(serializer.data, status=201)


@api_view(['GET', 'PUT', 'POST', 'DELETE'])  # complete::crud
def _see_about_this_api(request, annotation_id, *args, **kwargs):
    qs = get_object_or_404(Annotation, id=annotation_id, account=request.user)
    serializer = AnnotationSerializer(qs, many=False)
    return Response(serializer.data)


class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
