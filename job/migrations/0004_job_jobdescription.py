# Generated by Django 3.2.5 on 2021-07-24 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_jobjobtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='JOBDescription',
            field=models.TextField(default='', max_length=1000, verbose_name='Description'),
            preserve_default=False,
        ),
    ]
