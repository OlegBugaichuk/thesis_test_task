import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from company.tests.factories import UserFactory, DepartmentFactory, EmployeeFactory


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture
def api_client():
    return APIClient()


register(UserFactory)
register(DepartmentFactory)
register(EmployeeFactory)
