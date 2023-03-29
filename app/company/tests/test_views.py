from rest_framework import status


def test_departments_list_view(api_client, department_factory):
    DEPARTMENTS_COUNT = 5
    department_factory.create_batch(DEPARTMENTS_COUNT)
    response = api_client.get("/api/company/departments/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == DEPARTMENTS_COUNT


def test_employees_list(api_client, employee_factory, user):
    EMPLOYEES_COUNT = 5
    employee_factory.create_batch(EMPLOYEES_COUNT)
    api_client.force_login(user)
    response = api_client.get("/api/company/employees/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == EMPLOYEES_COUNT
