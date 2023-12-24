from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_auth.registration.views import SocialAccountListView
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="My API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('rest-auth/google/', SocialAccountListView.as_view()),
    # path('accounts/', include('allauth.urls')),
    
    # path("hello/", greeting.as_view(), name="greeting"),
    # path("register/", RegisterNewUser.as_view(),name="register"),
    # path("login/", obtain_auth_token,name="create_token"),


    path('team', TeamList.as_view()),
    path('team/<int:pk>', Team.as_view()),
    path('member', MemberList.as_view()),
    path('member/<int:pk>', Member.as_view()),
    path('rule', RuleList.as_view()),
    path('rule/<int:pk>', Rule.as_view()),
    path('felony', FelonyList.as_view()),
    path('felony/<int:pk>', Felony.as_view())
]