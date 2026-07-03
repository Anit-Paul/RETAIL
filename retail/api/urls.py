
from django.urls import path,include
from .views import LoginView, RegisterView, profileView

urlpatterns = [
    path('auth/register/',RegisterView.as_view(),name='register'),
    path('auth/login/',LoginView.as_view(),name='login'),
    path("auth/profile/", profileView.as_view(), name="profile"),
]
