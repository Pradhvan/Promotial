# Generated by Django 2.1.5 on 2019-01-10 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('name', models.CharField(max_length=1000)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=100)),
                ('campaign_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('impression', models.IntegerField(blank=True, null=True)),
                ('click', models.IntegerField(blank=True, null=True)),
                ('install', models.IntegerField(blank=True, null=True)),
                ('spend', models.IntegerField(blank=True, null=True)),
                ('ecpm', models.IntegerField(blank=True, null=True)),
                ('ecpi', models.IntegerField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
