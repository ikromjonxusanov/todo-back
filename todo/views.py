from . import models, serializers
from rest_framework.viewsets import ModelViewSet
# Create your views here.

def get_object_or_none(Model, pk):
    try:
        return Model.objects.get(id=pk)
    except:
        return None


class TodoViewSet(ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
   