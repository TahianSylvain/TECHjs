from rest_framework import serializers, generics
from rest_framework.authtoken.models import Token
from principal.models import Task, Annotation
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)


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
