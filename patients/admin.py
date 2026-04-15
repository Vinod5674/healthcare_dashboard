from django.contrib import admin

# Register your models here.
from .models import Patient, MedicalRecord, VitalRecord
admin.site.register(Patient)
admin.site.register(MedicalRecord)
admin.site.register(VitalRecord)

