from rest_framework import viewsets

from rest_framework import permissions

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]