from django.contrib import admin
from .models import Student

# Register your models here.
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    class Meta:
        model = Student

admin.site.register(Student,StudentModelAdmin)