# Generated by Django 5.0 on 2024-01-09 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mockapp', '0012_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10)),
                ('student_name', models.CharField(max_length=200)),
                ('contact_number', models.CharField(max_length=250)),
                ('test_taken', models.CharField(max_length=200)),
                ('mcq_marks', models.CharField(max_length=100)),
                ('coding_marks', models.TextField(max_length=100)),
            ],
        ),
    ]
