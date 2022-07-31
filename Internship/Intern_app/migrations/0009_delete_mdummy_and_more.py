# Generated by Django 4.0.2 on 2022-07-10 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intern_app', '0008_mdummy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='mdummy',
        ),
        migrations.AddField(
            model_name='assignment_details',
            name='Assignment_instructions',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='readingmaterial_details',
            name='ReadingMaterial_instructions',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='assignment_details',
            name='Assignment_content',
            field=models.FileField(upload_to='static/Intern_app'),
        ),
        migrations.AlterField(
            model_name='readingmaterial_details',
            name='ReadingMaterial_content',
            field=models.FileField(upload_to='static/Intern_app'),
        ),
    ]
