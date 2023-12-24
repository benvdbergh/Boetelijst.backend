from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response

from api.models import *
from api.serializers import *

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
        
class greeting(APIView):
    permission_classes = ( IsAuthenticated, )

    def get(self,request):
        content = {'message': 'Hello, {}!'.format(request.user.first_name)}
        return Response(content)


class TeamList(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class Team(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_url = 'team_id'

class MemberList(ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class Member(RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    lookup_url = 'member_id'

class RuleList(ListCreateAPIView):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

class Rule(RetrieveUpdateDestroyAPIView):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
    lookup_url = 'rule_id'

class FelonyList(ListCreateAPIView):
    queryset = Felony.objects.all()
    serializer_class = FelonySerializer

class Felony(RetrieveUpdateDestroyAPIView):
    queryset = Felony.objects.all()
    serializer_class = FelonySerializer
    lookup_url = 'felony_id'