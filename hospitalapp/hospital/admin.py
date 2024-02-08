from django.contrib import admin
from .models import Appointment, Prescription, Medication
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(Medication)
