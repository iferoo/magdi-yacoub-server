from rest_framework import serializers
from .models import *

class PatientSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = "__all__"
        depth = 2

class DoctorSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
        depth = 1

class NurseSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Nurse
        fields = "__all__"
        depth = 1

class BedSerilizer(serializers.ModelSerializer):
    Patient = PatientSerilizer(read_only=True)
    class Meta:
        model = Bed
        # fields = ['id', 'Number', 'Status', 'Patient']
        fields = ['__all__']
        depth = 1

class RoomSerilizer(serializers.ModelSerializer):
    Beds = BedSerilizer(read_only=True, many=True)
    class Meta:
        model = Room
        fields = "__all__"
        depth = 1

