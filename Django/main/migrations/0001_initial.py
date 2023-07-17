# Generated by Django 4.2.2 on 2023-07-16 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100, verbose_name='Автор теста')),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
