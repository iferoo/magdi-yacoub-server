from django.db import models
# Create your models here.


class Room(models.Model):
    Name = models.CharField(max_length=70, null=True)

class Bed(models.Model):
    RoomID = models.ForeignKey(Room, related_name='Beds', on_delete=models.CASCADE)

class Doctor(models.Model):
    Name = models.CharField(max_length=70, null=True)
    Age = models.IntegerField(null=True)
    Gender = models.CharField(max_length=70, null=True)
    Email = models.EmailField(max_length=70, null=True)
    Status = models.CharField(max_length=70, null=True)

class Nurse(models.Model):
    Name = models.CharField(max_length=70, null=True)
    Age = models.IntegerField(null=True)
    Gender = models.CharField(max_length=70, null=True)
    Email = models.EmailField(max_length=70, null=True)
    Status = models.CharField(max_length=70, null=True)

class Patient(models.Model):
    Name = models.CharField(max_length=70, null=True)
    Bed = models.OneToOneField(Bed, on_delete=models.SET_NULL, related_name='Patient', null=True)
    Status = models.CharField(max_length=70, null=True)
    Condition = models.CharField(max_length=70, null=True)
    Age = models.CharField(max_length=70, null=True)
    Gender = models.CharField(max_length=70, null=True)
    RegisterDate = models.CharField(max_length=70, null=True)
    Branch = models.CharField(max_length=70, null=True)
    Nurse = models.ForeignKey(Nurse, related_name='PatientNurse', on_delete=models.CASCADE)
    Doctor =  models.ForeignKey(Doctor, related_name='PatientDoctor', on_delete=models.CASCADE)
    Disease = models.CharField(max_length=70, null=True)
    History = models.CharField(max_length=70, null=True)
    OtherDiseases = models.CharField(max_length=70, null=True)
    Diabeyic = models.BooleanField(max_length=70, null=True)
    Smoker = models.BooleanField(max_length=70, null=True)