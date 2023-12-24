from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

from api.models import Team, Member, Rule, Felony

class CustomRegisterSerializer(RegisterSerializer):
    pass

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        lookup_field = 'id'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'

class FelonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Felony
        fields = '__all__'