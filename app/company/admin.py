from django.contrib import admin

from .models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    ...


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    ...
