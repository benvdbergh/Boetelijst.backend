# Generated by Django 3.2 on 2023-12-29 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_name', models.CharField(max_length=50)),
                ('team_handle', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('team_created_date', models.DateTimeField(auto_now_add=True)),
                ('team_modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_summary', models.CharField(max_length=256)),
                ('rule_description', models.CharField(max_length=256)),
                ('rule_fee', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rule_created_date', models.DateTimeField(auto_now_add=True)),
                ('rule_modified_date', models.DateTimeField(auto_now=True)),
                ('rule_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.team')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=50)),
                ('role_add_rule', models.BooleanField()),
                ('role_edit_rule', models.BooleanField()),
                ('role_delete_rule', models.BooleanField()),
                ('role_add_felony', models.BooleanField()),
                ('role_edit_felony', models.BooleanField()),
                ('role_delete_felony', models.BooleanField()),
                ('role_add_member', models.BooleanField()),
                ('role_delete_memeber', models.BooleanField()),
                ('role_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.team')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_position', models.CharField(choices=[('t', 'Trainer'), ('h', 'Receptie-Hoek'), ('m', 'Midden'), ('s', 'Setter'), ('o', 'Opposite'), ('l', 'Libero')], max_length=50)),
                ('member_created_date', models.DateTimeField(auto_now_add=True)),
                ('member_modified_date', models.DateTimeField(auto_now=True)),
                ('member_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.team')),
                ('member_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('member_user_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.role')),
            ],
        ),
        migrations.CreateModel(
            name='Felony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('felony_comment', models.CharField(max_length=256)),
                ('felony_initial_fee', models.DecimalField(decimal_places=2, max_digits=5)),
                ('felony_created_date', models.DateTimeField(auto_now_add=True)),
                ('felony_modified_date', models.DateTimeField(auto_now=True)),
                ('felony_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.member')),
                ('felony_rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.rule')),
                ('felony_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.team')),
            ],
        ),
    ]
