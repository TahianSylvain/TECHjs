from rest_framework import serializers
from principal.models import Task, Annotation


class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ( 
                    'id', 'account', 'name', 'description',
                    'description', 'deadline', 'reminder', 'over',
                    # 'get_nb_views', 'get_nb_likes', 'get_nb_unlikes'
                )


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'relation', 'action')
