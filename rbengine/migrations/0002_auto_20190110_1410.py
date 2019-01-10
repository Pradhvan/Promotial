# Generated by Django 2.1.5 on 2019-01-10 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbengine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='status',
        ),
        migrations.AddField(
            model_name='campaign',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2),
        ),
    ]