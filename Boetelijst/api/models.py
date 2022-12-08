from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email =  models.EmailField(max_length=254)
#     created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
#     modified_date = models.DateTimeField( auto_now=True, auto_now_add=False)

class UserRole(models.Model):
    role_name = models.CharField(max_length=50)
    role_permissions = models.JSONField()
    add_rule = models.BooleanField()
    edit_rule = models.BooleanField()
    delete_rule = models.BooleanField()
    add_felony = models.BooleanField()
    edit_felony = models.BooleanField()
    delete_felony = models.BooleanField()
    add_member = models.BooleanField()
    delete_memeber = models.BooleanField()

class Team(models.Model):
    team_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    
class Member(models.Model):
    pos_enum = (
        ('t', 'Trainer'),
        ('h', 'Receptie-Hoek'),
        ('m', 'Midden'),
        ('s', 'Setter'),
        ('o', 'Opposite'),
        ('l', 'Libero')
    )

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    position = models.CharField(max_length=50, choices=pos_enum)
    member_created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    member_modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

class Rule(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    summary = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    fee = models.DecimalField(max_digits=5, decimal_places=2)
    rule_created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    rule_modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

class Felony(models.Model):
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
    member = models.ForeignKey(Rule, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    initial_fee = models.DecimalField(max_digits=5, decimal_places=2)
    felony_created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    felony_modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)
