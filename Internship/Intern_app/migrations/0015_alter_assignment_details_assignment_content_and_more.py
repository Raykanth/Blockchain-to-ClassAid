# Generated by Django 4.0.2 on 2022-07-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intern_app', '0014_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment_details',
            name='Assignment_content',
            field=models.FileField(upload_to='static/Assignment_content'),
        ),
        migrations.AlterField(
            model_name='readingmaterial_details',
            name='ReadingMaterial_content',
            field=models.FileField(upload_to='static/ReadingMaterial_content'),
        ),
        migrations.AlterField(
            model_name='students_ass_submission',
            name='Submission_content',
            field=models.FileField(upload_to='static/Assignment_submissions'),
        ),
    ]
