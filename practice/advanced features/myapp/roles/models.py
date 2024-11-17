from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import MedicalRecord

# Create your models here.
class MedicalRecord(models.Model):
    name=models.CharField(max_length=100)
    
    

# ceating user groups which I will later assign roles to

doctor_group, create = Group.objects.get_or_create(name='doctor')
nurse_group, created = Group.objects.get_or_create(name='nurse')
patient_broup, created = Group.objects.get_or_create(name='patient')



# Example: Give 'Doctor' group permission to view, add, and change Medical Records
content_type = ContentType.objects.get_for_model(MedicalRecord)
permission_view = Permission.objects.get(content_type=content_type, codename='view_medicalrecord')
permission_add = Permission.objects.get(content_type=content_type, codename='add_medicalrecord')
permission_change = Permission.objects.get(content_type=content_type, codename='change_medicalrecord')

doctor_group.permissions.add(permission_view, permission_add, permission_change)


