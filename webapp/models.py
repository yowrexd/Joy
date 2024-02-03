from django.db import models

# Create your models here.
class PatientInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=False)
    gender = models.CharField(max_length=50)
    contact = models.IntegerField(blank=False)
    address = models.CharField(max_length=50)
    def __str__(self):
        return self.name
 
class MedicalHistory(models.Model):
    patientinfo = models.OneToOneField(PatientInfo, related_name='MedicalHistory', on_delete=models.CASCADE)
    patientinfo = models.ForeignKey(PatientInfo, on_delete=models.SET_NULL, null=True)
    med_history = models.CharField(max_length=50)
    allergies = models.CharField(max_length=50)
    
    def __str__(self):
        return self.med_history
    
class Appointment(models.Model):
    patientinfo = models.OneToOneField(PatientInfo, related_name='Appointment', on_delete=models.CASCADE)
    patientinfo = models.ForeignKey(PatientInfo, on_delete=models.SET_NULL, null=True)
    doctor = models.CharField(max_length=50)
    date =  models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    reason = models.CharField(max_length=50)
    
    def __str__(self):
        return self.doctor
    
class Prescription(models.Model):
    patientinfo = models.ForeignKey(PatientInfo, on_delete=models.SET_NULL, null=True)
    medicalhistory = models.ForeignKey(MedicalHistory, on_delete=models.SET_NULL, null=True)
    medication = models.CharField(max_length=50)
    dosage = models.IntegerField(blank=False)
    frequency = models.IntegerField(blank=False)
    patientinfo = models.OneToOneField(PatientInfo, related_name='Prescription', on_delete=models.CASCADE)
    def __str__(self):
        return self.medication
    
class InsuranceInformation(models.Model):
    patientinfo = models.OneToOneField(PatientInfo, related_name='InsuranceInformation', on_delete=models.CASCADE)
    patientinfo = models.ForeignKey(PatientInfo, on_delete=models.SET_NULL, null=True)
    insurance = models.CharField(max_length=50)
    details = models.CharField(max_length=50)
    
    def __str__(self):
        return self.insurance
    