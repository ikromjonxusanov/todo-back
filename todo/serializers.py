from . import models
from rest_framework import serializers

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TodoList
        fields = "__all__"
