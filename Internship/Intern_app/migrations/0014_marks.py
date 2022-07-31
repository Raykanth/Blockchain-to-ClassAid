# Generated by Django 4.0.2 on 2022-07-15 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intern_app', '0013_delete_marks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=30)),
                ('Course_name', models.CharField(max_length=30)),
                ('Assignment_id', models.CharField(max_length=30)),
                ('Content', models.CharField(max_length=100)),
                ('Person1_name', models.CharField(max_length=30)),
                ('Marks1', models.CharField(max_length=30)),
                ('Person2_name', models.CharField(max_length=30)),
                ('Marks2', models.CharField(max_length=30)),
                ('Person3_name', models.CharField(max_length=30)),
                ('Marks3', models.CharField(max_length=30)),
                ('Total', models.CharField(max_length=30)),
            ],
        ),
    ]
