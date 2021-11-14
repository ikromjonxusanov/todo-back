from . import models
from rest_framework import serializers

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TodoList
        fields = "__all__"
"""
{
"title":"Title 1",
"content": "Content 1",
"created":"2021-11-12",
"due_date":"2021-11-15",
"category":{
    "id":1
  }
}
"""