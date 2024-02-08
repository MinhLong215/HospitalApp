from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('patient', 'Patient'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    phone_number = models.CharField(max_length=20, blank=True, null=True)  # Thêm trường số điện thoại
    date_of_birth = models.DateTimeField(blank=True, null=True)


#Bác Sĩ
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialization = models.CharField(max_length=100)#chuyên môn

#Y Tá
class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nurse_profile')
    department = models.CharField(max_length=100) #bộ phận

#Bệnh nhân
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    avatar = CloudinaryField('avatar', null=True)
    # Thêm các trường khác tương ứng với thông tin của bệnh nhân

#Lịch Khám
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField() #lịch khám
    symptoms = models.TextField()  # triệu chứng
    type_of_disease = models.CharField(max_length=100) #loại bệnh
    is_confirmed = models.BooleanField(default=False) #boolean xác nhận


#Toa Thuốc
class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='prescription') #lịch khám
    diagnosis = models.CharField(max_length=100) #kết luận/chẩn đoán
    precepts = models.TextField() #lời dặn
    medications = models.ManyToManyField('Medication', related_name='prescriptions')#danh mục thuốc uống

#Thuốc
class Medication(models.Model):
    name = models.CharField(max_length=100, null=False) #tên thuốc
    description = RichTextField() #miêu tả
    image = models.ImageField(upload_to='medications/%Y/%m') #ảnh
    # Thêm các trường khác tương ứng với thông tin của thuốc

    def __str__(self):
        return self.name

#Hóa Đơn
class Payment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)#tien kham
    prescription = models.OneToOneField(Prescription, on_delete=models.CASCADE)#chi phí toa thuốc
    payment_method = models.CharField(max_length=50)#phương thức thanh toán
    payment_time = models.DateTimeField(auto_now_add=True)#thời gian thanh toán
