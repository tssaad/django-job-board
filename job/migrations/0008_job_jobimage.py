# Generated by Django 3.2.3 on 2021-07-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_job_jobcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='JOBImage',
            field=models.ImageField(blank=True, null=True, upload_to='jobs/', verbose_name='Image'),
        ),
    ]
