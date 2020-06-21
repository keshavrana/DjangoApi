from rest_framework import serializers

from .models import Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'description','created','updated')