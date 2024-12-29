from django.urls import path
from .views import TaskListCreateAPIView, TaskDetailAPIView

urlpatterns = [
    path('projects/<uuid:project_id>/tasks/', TaskListCreateAPIView.as_view(), name='task_list_create'),
    path('tasks/<uuid:task_id>/', TaskDetailAPIView.as_view(), name='task_detail'),
]
