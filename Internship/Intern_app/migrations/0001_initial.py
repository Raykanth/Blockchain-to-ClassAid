# Generated by Django 4.0.2 on 2022-07-08 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login_Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=30)),
                ('Student_pass', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Login_Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher_name', models.CharField(max_length=30)),
                ('Teacher_pass', models.CharField(max_length=30)),
            ],
        ),
    ]