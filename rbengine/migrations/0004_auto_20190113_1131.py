# Generated by Django 2.1.5 on 2019-01-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbengine', '0003_auto_20190111_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='ACTION',
            field=models.CharField(choices=[('Notify', 'Notify'), ('Start', 'Start'), ('Pause', 'Pause')], default='Notify', max_length=1000),
        ),
        migrations.AlterField(
            model_name='rule',
            name='STATUS',
            field=models.CharField(choices=[('Activate', 'Activate'), ('Deactivate', 'Deactivate')], default='Activate', max_length=1000),
        ),
    ]
