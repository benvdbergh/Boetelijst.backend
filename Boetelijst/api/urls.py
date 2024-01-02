from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_auth.registration.views import SocialAccountListView
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from rest_framework_simplejwt import views as jwt_views

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

    path('team', TeamListView.as_view()),
    path('team/<int:pk>', TeamView.as_view()),
    path('<str:team_handle>/role', RoleListView.as_view()),
    path('<str:team_handle>/role/<int:pk>', RoleView.as_view()),
    path('<str:team_handle>/member', MemberListView.as_view()),
    path('<str:team_handle>/member/<int:pk>', MemberView.as_view()),
    path('<str:team_handle>/rule', RuleListView.as_view()),
    path('<str:team_handle>/rule/<int:pk>', RuleView.as_view()),
    path('<str:team_handle>/felony', FelonyListView.as_view()),
    path('<str:team_handle>/felony/<int:pk>', FelonyView.as_view()),
    path('token', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('logout', LogoutView.as_view(), name ='logout')
]