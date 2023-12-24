from django.db import models

class UserRole(models.Model):
    role_name = models.CharField(max_length=50)
    role_permissions = models.JSONField()
    role_add_rule = models.BooleanField()
    role_edit_rule = models.BooleanField()
    role_delete_rule = models.BooleanField()
    role_add_felony = models.BooleanField()
    role_edit_felony = models.BooleanField()
    role_delete_felony = models.BooleanField()
    role_add_member = models.BooleanField()
    role_delete_memeber = models.BooleanField()

class Team(models.Model):
    team_name = models.CharField(max_length=50)
    team_created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    team_modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    
class Member(models.Model):
    pos_enum = (
        ('t', 'Trainer'),
        ('h', 'Receptie-Hoek'),
        ('m', 'Midden'),
        ('s', 'Setter'),
        ('o', 'Opposite'),
        ('l', 'Libero')
    )

    member_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # member_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    member_user_name = models.CharField(max_length=50)
    member_user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    member_position = models.CharField(max_length=50, choices=pos_enum)
    member_created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    member_modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

class Rule(models.Model):
    rule_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    rule_summary = models.CharField(max_length=256)
    rule_description = models.CharField(max_length=256)
    rule_fee = models.DecimalField(max_digits=5, decimal_places=2)
    rule_created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    rule_modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

class Felony(models.Model):
    felony_rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
    felony_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    felony_member = models.ForeignKey(Member, on_delete=models.CASCADE)
    felony_comment = models.CharField(max_length=256)
    felony_initial_fee = models.DecimalField(max_digits=5, decimal_places=2)
    felony_created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    felony_modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)
