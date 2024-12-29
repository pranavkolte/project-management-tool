from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Projects
from .serializers import ProjectSerializer
from django.shortcuts import get_object_or_404

class ProjectAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Projects.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(
            data={
                "message": "Projects Found",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        owner = request.data.get('owner', request.user.user_id)
        request_data = request.data.copy()
        request_data['owner'] = owner

        serializer = ProjectSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    "message": "Project created",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            data={
                "exception": f"{serializer.errors}",
                "message": "Something went wrong",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

class ProjectDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, project_id):
        project = get_object_or_404(Projects, project_id=project_id)
        serializer = ProjectSerializer(project)
        return Response(
            data={
                "message": "Project/s Found",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def patch(self, request, project_id):
        project = get_object_or_404(Projects, project_id=project_id)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    "message": "Project Updated",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            data={
                "exception": f"{serializer.errors}",
                "message": "Something went wrong",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, project_id):
        project = get_object_or_404(Projects, project_id=project_id)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
