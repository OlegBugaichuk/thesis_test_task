from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Department(models.Model):
    name = models.CharField("Название", max_length=100)
    director = models.ForeignKey(
        "Employee",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="managed_departments",
    )

    class Meta:
        verbose_name = "Департамент"
        verbose_name_plural = "Департаменты"

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100, db_index=True)
    patronymic = models.CharField("Отчество", max_length=100, blank=True)
    photo = models.ImageField("Фото", upload_to="employees/photos/")
    position = models.CharField("Должность", max_length=100)
    salary = models.DecimalField(
        "Оклад", max_digits=8, decimal_places=2, validators=(MinValueValidator(0.00),)
    )
    age = models.PositiveIntegerField("Возраст", validators=(MaxValueValidator(200),))
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="employees"
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic} | {self.position}"
