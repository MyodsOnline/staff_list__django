from rest_framework import serializers

from .models import Staff, Substation, Organization


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class SubstationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Substation
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
