from django.urls import path
from rest_framework import routers

from .views import (
    TodoView,
)

router = routers.DefaultRouter()

router.register(r'todos', TodoView, basename='todo')




urlpatterns = router.urls