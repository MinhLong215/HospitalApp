from django.contrib import admin
from django.utils.html import mark_safe
from .models import Appointment, Prescription, Medication
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# class MedicationForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorUploadingWidget)
#     class Meta:
#     model = Medication
#     fields = '__all__'
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id']

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['id']

class MedicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
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
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(Medication, MedicationAdmin)
