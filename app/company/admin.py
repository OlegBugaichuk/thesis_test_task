from django.contrib import admin

from company.models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    ...


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    ...
