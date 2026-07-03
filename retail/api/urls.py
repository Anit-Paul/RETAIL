
from django.urls import path,include
from .views import RegisterView

urlpatterns = [
    path('auth/register/',RegisterView.as_view(),name='register')
]
