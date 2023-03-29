from rest_framework import generics, viewsets, mixins
from django.db.models import Sum, Count

from company.models import Department, Employee
from company.serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.annotate(
        employees_count=Count('employees')
    ).annotate(
        employees_salary_sum=Sum('employees__salary')
    )
    serializer_class = DepartmentSerializer


class EmployeeViewSet(mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
