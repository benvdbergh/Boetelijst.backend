from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import *
from api.serializers import *

import logging

logger = logging.getLogger(__name__)

class RegisterNewUser(APIView):
    def post(self,request):
        username = request.data.get("username")
        email = request.data.get("email")
        name = request.data.get("name")
        
        try:
            user  = User.objects.create_user(
                username = username,
                password = "random123",
                email = email,
                first_name = name,
            )
            user.save()
            print("{} created successfully".format(user.username))
            return Response({"message":"User created"})
        except:
            return Response({"message":"User creation failed or user already exists"})


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):    
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class TeamListView(ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        team_handle = self.request.data.get('team_handle')
        if not team_handle or team_handle.strip() == "":
            team_name = self.request.data.get('team_name')
            team_handle = team_name.replace(" ", "")[:10].lower()  # Remove spaces and make fully lowercase
            existing_handles = Team.objects.filter(team_handle__startswith=team_handle).count()
            if existing_handles > 0:
                team_handle += str(existing_handles)  # Add integer if handle exists

        serializer.save(team_handle=team_handle)
        return super().perform_create(serializer) 

class TeamView(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_url = 'team_handle'

class RoleListView(ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get_queryset(self):
        team_handle = self.kwargs.get('team_handle')
        return Role.objects.filter(team_handle=team_handle)

    def perform_create(self, serializer):
        team_handle = self.kwargs.get('team_handle')
        logger.debug(team_handle)
        team = Team.objects.get(team_handle=team_handle)
        serializer.save(role_team=team)
        return super().perform_create(serializer)

class RoleView(RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    lookup_url = 'role_id'

class MemberListView(ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get_queryset(self):
        team_handle = self.kwargs.get('team_handle')
        return Member.objects.filter(team_handle=team_handle)

    def perform_create(self, serializer):
        # Access user information using request.user
        try:
            user = self.request.user
            logger.debug("Debugger active")
            logger.debug(user.id)

            team_handle = self.kwargs.get('team_handle')
            team = Team.objects.get(team_handle=team_handle)
            logger.debug(team.team_handle)
            # Your logic here
            serializer.save(member_user_id=user.id, member_team_id=team.team_handle)

        except Exception as e:
            logger.error(e)

        return super().perform_create(serializer)


class MemberView(RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    lookup_url = 'member_id'

class RuleListView(ListCreateAPIView):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

    def get_queryset(self):
        team_handle = self.kwargs.get('team_handle')
        return Rule.objects.filter(team_handle=team_handle)

class RuleView(RetrieveUpdateDestroyAPIView):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
    lookup_url = 'rule_id'

class FelonyListView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Felony.objects.all()
    serializer_class = FelonySerializer

    def get_queryset(self):
        team_handle = self.kwargs.get('team_handle')
        return Felony.objects.filter(team_handle=team_handle)

    def perform_create(self, serializer):
        # Access user information using request.user
        user = self.request.user
        # Your logic here
        serializer.save(user=user)

class FelonyView(RetrieveUpdateDestroyAPIView):
    queryset = Felony.objects.all()
    serializer_class = FelonySerializer
    lookup_url = 'felony_id'