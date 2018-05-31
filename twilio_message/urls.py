from django.urls import path
from . import views

urlpatterns = [
    path('', views.SendMessageView.as_view())
]
