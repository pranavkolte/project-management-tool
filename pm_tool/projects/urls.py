from django.urls import path
from .views import ProjectAPIView, ProjectDetailAPIView

urlpatterns = [
    path("", ProjectAPIView.as_view(), name="project_list_create"),
    path("<uuid:project_id>/", ProjectDetailAPIView.as_view(), name="project_detail"),
]
