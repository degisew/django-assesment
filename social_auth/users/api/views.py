from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from social_auth.users.permissions import IsAdmin, IsCoach, IsAgent, IsFootballPlayer
from django.conf import settings
from django.http import HttpResponseRedirect


# def email_confirm_redirect(request, key):
#     return HttpResponseRedirect(
#         f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{key}/"
#     )


def password_reset_confirm_redirect(request, uidb64, token):
    return HttpResponseRedirect(
        f"{settings.PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL}{uidb64}/{token}/"
    )

class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({"message": "Welcome, Admin!"})


class CoachOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsCoach]

    def get(self, request):
        return Response({"message": "Welcome, Coach!"})


class AgentOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAgent]

    def get(self, request):
        return Response({"message": "Welcome, Agent!"})


class FootballPlayerOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsFootballPlayer]

    def get(self, request):
        return Response({"message": "Welcome, Football Player!"})
