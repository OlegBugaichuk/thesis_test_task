from rest_framework import generics, viewsets, mixins
from rest_framework import filters
from django.db.models import Sum, Count

from company.models import Department, Employee
from company.serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentListView(generics.ListAPIView):
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        return Department.objects.annotate(
            employees_count=Count('employees')
        ).annotate(
            employees_salary_sum=Sum('employees__salary')
        )


class EmployeeViewSet(mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["last_name", "department__id"]
