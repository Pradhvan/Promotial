from django.conf import settings
from django.db import models
from django.utils import timezone


class Campaign(models.Model):
    name = models.CharField(max_length=1000)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    Activate = 'ACT'
    Stop = 'Stop'
    Pause = 'Pa'
    STATUS_CHOICES = (
        (Activate, 'Activate'),
        (Stop, 'Stop'),
        (Pause, 'Pause'),
    )
    STATUS = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=Activate,
    )
    campaign_id = models.CharField(primary_key=True, max_length=100)
    # List of metrics
    impression = models.IntegerField(blank=True, null=True)
    click = models.IntegerField(blank=True, null=True)
    install = models.IntegerField(blank=True, null=True)
    spend = models.IntegerField(blank=True, null=True)
    ecpm = models.IntegerField(blank=True, null=True)
    ecpi = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name, self.status
