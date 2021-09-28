from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReadySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ready
        fields = "__all__"


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormData
        fields = "__all__"

    def create(self, validated_data):
        data = FormData(
            name=validated_data['mail'],
            phone=validated_data['phone'],
            mail=validated_data['mail'],
            textData=validated_data['textData'],
            file=validated_data['file']
        )
        data.save()
        return data


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'

    def create(self, validated_data):
        user = Person(
            email=validated_data['email'],
            phone=validated_data['phone'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user