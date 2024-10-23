from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from allauth.socialaccount.views import signup
from social_auth.users.api.views import GoogleLogin
from dj_rest_auth.views import (
    PasswordResetConfirmView,
    PasswordResetView,
)
from django.urls import path
from social_auth.users.api.views import password_reset_confirm_redirect

from social_auth.users.api.views import (
    AdminOnlyView,
    CoachOnlyView,
    AgentOnlyView,
    FootballPlayerOnlyView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
    path("password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path(
        "password/reset/confirm/<str:uidb64>/<str:token>/",
        password_reset_confirm_redirect,
        name="password_reset_confirm",
    ),
    path(
        "password/reset/confirm/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),

    path("signup/", signup, name="socialaccount_signup"),
    path("google/", GoogleLogin.as_view(), name="google_login"),

    path('admin/', AdminOnlyView.as_view(), name='admin'),
    path('coach/', CoachOnlyView.as_view(), name='coach'),
    path('agent/', AgentOnlyView.as_view(), name='agent'),
    path('player/', FootballPlayerOnlyView.as_view(), name='player'),
]
