from django.db.models import Sum, Count

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from company.models import Department, Employee
from company.serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentListView(ListAPIView):
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        return Department.objects.annotate(
            employees_count=Count('employees')
        ).annotate(
            employees_salary_sum=Sum('employees__salary')
        )


class EmployeeViewSet(ListModelMixin,
                      DestroyModelMixin,
                      CreateModelMixin,
                      GenericViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [SearchFilter]
    search_fields = ["last_name", "department__id"]
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
