from rest_framework import routers
from rest_framework.routers import SimpleRouter
from todo.views import TodoViewSet
router = routers.SimpleRouter()
router.register('todo', TodoViewSet, basename="todolist")
urlpatterns = router.urls
