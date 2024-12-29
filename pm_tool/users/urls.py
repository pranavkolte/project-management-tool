from django.urls import path
from .views import UserRegistrationAPIView, CustomTokenObtainPairView, CustomTokenRefreshView, UserDetailAPIView

urlpatterns = [
    path("register/", UserRegistrationAPIView.as_view(), name="user_registration"),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("<uuid:user_id>/", UserDetailAPIView.as_view(), name="user_detail"),
]
