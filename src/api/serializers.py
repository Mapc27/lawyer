from rest_framework import serializers
from web.models import Application, SolvedApplication


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"


class SolvedApplicationViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolvedApplication
        fields = "__all__"
