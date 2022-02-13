from rest_framework import serializers
from web.models import Application, SolvedApplication


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('phone_number', 'person_name', 'description')


class ApplicationViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'phone_number', 'person_name', 'description')


class SolvedApplicationViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolvedApplication
        fields = ('id', 'title', 'history', 'result')
