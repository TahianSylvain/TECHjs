from django.http import JsonResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from principal.models import Annotation, Task
from django.shortcuts import get_object_or_404
from principal.serializers import AnnotationSerializer, TaskSerializer


@api_view(['GET', 'PUT', 'POST'])  # read, update, create
def _see_your_apis(request, *args, **kwargs):
    qs = Annotation.objects.filter(account=request.user).order_by('-deadline')
    serializer = AnnotationSerializer(qs, many=True)
    print(serializer.data, *args, **kwargs)
    return Response(serializer.data, status=201)


@api_view(['GET', 'PUT', 'POST', 'DELETE'])  # complete::crud
def _see_about_this_api(request, annotation_id, *args, **kwargs):
    qs = get_object_or_404(Annotation, id=annotation_id, account=request.user)
    serializer = AnnotationSerializer(qs, many=False)
    print(qs, *args, **kwargs)
    return Response(serializer.data)


class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
