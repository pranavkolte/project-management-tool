from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from .models import Users
from .serializers import (
    CustomTokenObtainPairSerializer,
    CustomTokenRefreshSerializer,
    UserRegistrationSerializer,
    UserDetailSerializer
)


# Create your views here.
class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                data={
                    "data" : {
                        "id": user.user_id,
                        "username": user.username,
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "created_at": user.date_joined,
                    },
                    "message": "User registered successfully"
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            data={
                "exception": f"{serializer.errors}",
                "message": "Something went wrong",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class UserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user = get_object_or_404(Users, user_id=user_id)
        serializer = UserDetailSerializer(user)
        return Response(
            data={
                "message": "User Found",
                "data":serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def patch(self, request, user_id):
        user = get_object_or_404(Users, user_id=user_id)
        serializer = UserRegistrationSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    "message": "User Updated",
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

    def delete(self, request, user_id):
        user = get_object_or_404(Users, user_id=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    