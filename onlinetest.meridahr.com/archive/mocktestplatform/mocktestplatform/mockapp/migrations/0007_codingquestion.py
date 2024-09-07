# Generated by Django 5.0 on 2024-01-05 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mockapp', '0006_bootstrap_question_css_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodingQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('code_snippet', models.TextField()),
                ('correct_answer', models.TextField()),
            ],
        ),
    ]