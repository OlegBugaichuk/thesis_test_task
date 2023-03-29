from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import DepartmentListView, EmployeeViewSet

urlpatterns = [
    path("departments/", DepartmentListView.as_view()),
]

employee_router = DefaultRouter()
employee_router.register(r"employees", EmployeeViewSet)

urlpatterns += employee_router.urls
