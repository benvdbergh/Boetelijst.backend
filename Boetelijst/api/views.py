from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from api.models import *
from api.serializers import *

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class Team(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_url = 'team_id'

class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class Member(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    lookup_url = 'member_id'

class RuleList(generics.ListCreateAPIView):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

class Rule(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
    lookup_url = 'rule_id'

class FelonyList(generics.ListCreateAPIView):
    queryset = Felony.objects.all()
    serializer_class = FelonySerializer

class Felony(generics.RetrieveUpdateDestroyAPIView):
    queryset = Felony.objects.all()
    serializer_class = FelonySerializer
    lookup_url = 'felony_id'