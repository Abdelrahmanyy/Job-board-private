# Generated by Django 4.2.2 on 2023-06-27 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0002_job_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='jobs/%y/%m/%d'),
        ),
    ]