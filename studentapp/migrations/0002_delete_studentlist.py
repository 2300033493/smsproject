# Generated by Django 5.0.7 on 2024-10-14 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0003_alter_addcourse_student_alter_marks_student'),
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentList',
        ),
    ]