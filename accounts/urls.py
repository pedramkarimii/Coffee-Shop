from django.urls import path
from .views import (
    UserLoginView,
    UserLogoutView,
    EditeUserView,
    RegisterView,
    CreateUserView,
    ChangePasswordView,
    CreateProfileView,
    HomeView,
    ProfileDetailView,
)

""" 
URL pattern for the home page
URL pattern for user login
URL pattern for user logout
URL pattern for creating a user
URL pattern for creating a profile
URL pattern for editing a user
URL pattern for user registration
URL pattern for changing password 
URL pattern for Info profile 
URL pattern for ContactUS 
"""
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("creatuser/", CreateUserView.as_view(), name="creat_user"),
    path("creatprofile/", CreateProfileView.as_view(), name="creat_profile"),
    path("editeuser/", EditeUserView.as_view(), name="edit_user"),
    path("register/", RegisterView.as_view(), name="register"),
    path("changepass/", ChangePasswordView.as_view(), name="change_pass"),
    path("profiles/<int:pk>/", ProfileDetailView.as_view(), name="profile_detail"),
]
