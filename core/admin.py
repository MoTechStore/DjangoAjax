from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    pass
