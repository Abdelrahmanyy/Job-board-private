# Generated by Django 4.2.2 on 2023-08-06 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0007_alter_apply_cover_letter_alter_apply_cv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='Job.job'),
        ),
    ]
