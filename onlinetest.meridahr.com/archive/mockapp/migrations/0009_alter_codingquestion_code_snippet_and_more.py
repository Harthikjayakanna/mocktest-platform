# Generated by Django 5.0 on 2024-01-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mockapp', '0008_codingquestion_subject_codingquestion_test_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codingquestion',
            name='code_snippet',
            field=models.TextField(default='code_snippet'),
        ),
        migrations.AlterField(
            model_name='codingquestion',
            name='correct_answer',
            field=models.TextField(default='correct_answer'),
        ),
        migrations.AlterField(
            model_name='codingquestion',
            name='question_text',
            field=models.TextField(default='question_text'),
        ),
    ]