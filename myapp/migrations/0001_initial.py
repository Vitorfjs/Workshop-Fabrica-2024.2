# Generated by Django 5.1 on 2024-08-23 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=10)),
                ('mass', models.CharField(max_length=10)),
                ('hair_color', models.CharField(max_length=20)),
                ('skin_color', models.CharField(max_length=20)),
                ('eye_color', models.CharField(max_length=20)),
                ('birth_year', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
