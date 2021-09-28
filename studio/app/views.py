from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render


from .serializer import *
from .models import Case, Review, Person
from .permission import IsOwnerProfileOrReadOnly


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CaseListView(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


class FormCreateView(generics.CreateAPIView):
    queryset=FormData.objects.all()
    serializer_class=FormSerializer
    

class PersonCreateView(generics.ListCreateAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    permission_classes=[IsAuthenticated]

class PersonDetailView(generics.RetrieveUpdateAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]