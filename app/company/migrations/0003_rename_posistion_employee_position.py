# Generated by Django 4.1.7 on 2023-03-29 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_employee_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='posistion',
            new_name='position',
        ),
    ]
