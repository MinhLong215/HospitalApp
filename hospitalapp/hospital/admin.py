from django.contrib import admin
from django.utils.html import mark_safe
from .models import Appointment, Prescription, Medication, Doctor, Nurse, Patient, User, Payment, DutySchedule
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class HospitalAppAdminSite(admin.AdminSite):
    site_header = 'Clinic Management System'

    # def get_urls(self):
    #     return [
    #         path('course-stats/', self.stats_view)
    #     ] + super().get_urls()

    # def stats_view(self, request): //dùng làm báo cáo thống kê
        #pass

admin_site = HospitalAppAdminSite(name='myhospitalapp')


# class MedicationForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorUploadingWidget)
#     class Meta:
#     model = Medication
#     fields = '__all__'

# class AppointmentAdmin(admin.ModelAdmin):
#     list_display = ['id']
#
# class PrescriptionAdmin(admin.ModelAdmin):
#     list_display = ['id']

class PatientAdmin(admin.ModelAdmin):
    readonly_fields = ['avt']

    def avt(self, patient):
        if patient.avatar:
            return mark_safe(
                '<img src="{url}" width="120" />' \
                    .format(url=patient.avatar.url)
            )

class MedicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description','price']
    search_fields = ['name']
    list_filter = ['id', 'name']
    readonly_fields = ['img']

    def img(self, medication):
        if medication:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=medication.image.name)
            )

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

# Register your models here.
admin_site.register(Appointment)
admin_site.register(Prescription)
admin_site.register(Medication, MedicationAdmin)
admin_site.register(DutySchedule)
admin_site.register(Doctor)
admin_site.register(Nurse)
admin_site.register(Patient, PatientAdmin)
admin_site.register(User)
