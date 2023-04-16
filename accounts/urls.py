from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    ProfileListView,
    ProfileDetailView,
    RegistrationView,
    LoginView,
    VerifyEmail,
    PasswordResetRequest,
    PasswordResetConfirm,
)

urlpatterns = [
    path("<int:pk>/", ProfileDetailView.as_view(), name="profile_detail"),
    path("", ProfileListView.as_view(), name="profile_list"),
    path("register/", RegistrationView.as_view(), name="register"),
    path("verify-email/", VerifyEmail.as_view(), name="verify-email"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "password-reset-request/",
        PasswordResetRequest.as_view(),
        name="password-reset-request",
    ),
    path(
        "password-reset-confirm/",
        PasswordResetConfirm.as_view(),
        name="password-reset-confirm",
    ),
]
