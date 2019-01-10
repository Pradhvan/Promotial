# Generated by Django 2.1.5 on 2019-01-10 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbengine', '0002_auto_20190110_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='year_in_school',
        ),
        migrations.AddField(
            model_name='campaign',
            name='STATUS',
            field=models.CharField(choices=[('ACT', 'Activate'), ('Stop', 'Stop'), ('Pa', 'Pause')], default='ACT', max_length=2),
        ),
    ]
