# Generated by Django 3.2.5 on 2021-07-24 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': 'Job', 'verbose_name_plural': 'Jobs'},
        ),
        migrations.RenameField(
            model_name='job',
            old_name='title',
            new_name='JOBTitle',
        ),
    ]
