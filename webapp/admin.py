from django.contrib import admin
from .models import PatientInfo, MedicalHistory, Appointment, Prescription, InsuranceInformation
# Register your models here.
admin.site.register(PatientInfo)
admin.site.register(MedicalHistory)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(InsuranceInformation)
