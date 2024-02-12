from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import ArrayField

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('patient', 'Patient'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    phone_number = models.CharField(max_length=20, blank=True, null=True)  # Thêm trường số điện thoại
    date_of_birth = models.DateField(blank=True, null=True)


#Bác Sĩ
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialization = models.CharField(max_length=100)#chuyên môn

    def __str__(self):
        return self.user.username

#Y Tá
class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nurse_profile')
    department = models.CharField(max_length=100) #bộ phận

    def __str__(self):
        return self.user.username

#Bệnh nhân
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    avatar = CloudinaryField('avatar', null=True)
    # Thêm các trường khác tương ứng với thông tin của bệnh nhân

    def __str__(self):
        return self.user.username

#lịch trực
class DutySchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='duty_schedules_doctor')
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='duty_schedules_nurse')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Duty Schedule: Doctor - {str(self.doctor.user)}, Nurse - {str(self.nurse.user)}, Time: {self.start_time.strftime('%Y-%m-%d %H:%M')} - {self.end_time.strftime('%Y-%m-%d %H:%M')}"


#Lịch Khám
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField() #lịch khám
    symptoms = RichTextField()  # triệu chứng
    type_of_disease = models.CharField(max_length=100) #loại bệnh
    is_confirmed = models.BooleanField(default=False) #boolean xác nhận

    def __str__(self):
        return f"Appointment: Doctor - {str(self.doctor.user)}, Patient - {str(self.patient.user)}, Scheduled Time: {self.scheduled_time.strftime('%Y-%m-%d %H:%M')}"

#Toa Thuốc
class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='prescription') #lịch khám
    diagnosis = models.CharField(max_length=100) #kết luận/chẩn đoán
    precepts = RichTextField() #lời dặn
    medications = models.ManyToManyField('Medication', related_name='prescriptions')#danh mục thuốc uống

    @property
    def total_cost(self):
        return sum(medication.price for medication in self.medications.all())

    def __str__(self):
        return f"Prescription for {self.appointment.patient.user.username} at {self.appointment.scheduled_time}"


#Thuốc
class Medication(models.Model):
    name = models.CharField(max_length=100, null=False) #tên thuốc
    description = models.TextField() #miêu tả
    image = models.ImageField(upload_to='medications/%Y/%m') #ảnh
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # giá thuốc

    def __str__(self):
        return self.name

#Hóa Đơn
class Payment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)#tien kham
    prescription = models.OneToOneField(Prescription, on_delete=models.CASCADE)#chi phí toa thuốc
    payment_method = models.CharField(max_length=50)#phương thức thanh toán
    payment_time = models.DateTimeField(auto_now_add=True)#thời gian thanh toán

    @property
    def total_payment(self):
        total = self.amount
        if self.prescription:
            total += self.prescription.total_cost
        return total

    def __str__(self):
        return f"Payment for {self.patient.user.username} - Total: {self.total_payment}"


