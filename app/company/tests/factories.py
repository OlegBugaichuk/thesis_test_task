from company.models import Department, Employee
from django.contrib.auth import get_user_model
from factory import LazyFunction, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

UserModel = get_user_model()
fake = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = UserModel

    username = LazyFunction(fake.name)
    first_name = LazyFunction(fake.name)
    last_name = LazyFunction(fake.name)


class DepartmentFactory(DjangoModelFactory):
    class Meta:
        model = Department

    name = LazyFunction(fake.company)


class EmployeeFactory(DjangoModelFactory):
    class Meta:
        model = Employee

    first_name = LazyFunction(fake.name)
    last_name = LazyFunction(fake.name)
    patronymic = LazyFunction(fake.name)
    department = SubFactory(DepartmentFactory)
    photo = LazyFunction(fake.image_url)
    position = LazyFunction(fake.job)
    salary = fake.pydecimal(left_digits=6, right_digits=2)
    age = fake.pyint(min_value=1, max_value=250)
