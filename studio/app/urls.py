from django.urls import path

from . import views
from .models import *

urlpatterns = [
    path('case/', views.CaseListView.as_view()),
    path('review/', views.ReviewListView.as_view()),
    path('review/post/', views.ReviewCreateView.as_view()),
    path('form/', views.FormCreateView.as_view()),
    #gets all user profiles and create a new profile
    path("profile/",views.PersonCreateView.as_view(),name="profile"),
    #retrieves profile details of the currently logged in user
    path("profile/<int:pk>",views.PersonDetailView.as_view(),name="profile"),
]