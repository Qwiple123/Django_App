# Generated by Django 4.2.2 on 2023-07-17 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_test_questions_list_test_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_type',
        ),
    ]
