from django.contrib import admin
from .models import Appointment, Prescription, Medication
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class MedicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(Medication, MedicationAdmin)
