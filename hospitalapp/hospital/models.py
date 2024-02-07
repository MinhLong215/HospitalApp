from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('patient', 'Patient'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

#Bác Sĩ
class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='doctor_profile')
    specialization = models.CharField(max_length=100)#chuyên môn

#Y Tá
class Nurse(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='nurse_profile')
    department = models.CharField(max_length=100)#bộ phận

#Bệnh nhân
class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='patient_profile')
    avatar = CloudinaryField('avatar', null=True)
    # Thêm các trường khác tương ứng với thông tin của bệnh nhân

#Lịch Khám
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)

#Toa Thuốc
class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='prescription') #lịch khám
    symptoms = models.TextField() #triệu chứng
    diagnosis = models.TextField() #kết luận
    medications = models.ManyToManyField('Medication', related_name='prescriptions')#danh mục thuốc uống

#Thuốc
class Medication(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() #miêu tả
    # Thêm các trường khác tương ứng với thông tin của thuốc
