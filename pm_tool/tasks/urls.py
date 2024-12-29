from django.urls import path
from .views import TaskListCreateAPIView, TaskDetailAPIView, CommentListCreateAPIView, CommentDetailAPIView

urlpatterns = [
    path('projects/<uuid:project_id>/tasks/', TaskListCreateAPIView.as_view(), name='task_list_create'),
    path('tasks/<uuid:task_id>/', TaskDetailAPIView.as_view(), name='task_detail'),
    path('tasks/<uuid:task_id>/comments/', CommentListCreateAPIView.as_view(), name='comment_list_create'),
    path('comments/<uuid:comment_id>/', CommentDetailAPIView.as_view(), name='comment_detail'),
]
