from rest_framework import routers
from rest_framework.routers import SimpleRouter
from todo.views import TodoListViewSet
router = routers.SimpleRouter()
router.register('todo', TodoListViewSet, basename="todolist")
urlpatterns = router.urls
