from rest_framework import serializers
from . models import customer


class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ['First_Name', 'Last_Name', 'email']
