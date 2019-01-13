from django.conf import settings
from django.db import models
from django.utils import timezone


class Campaign(models.Model):
    name = models.CharField(max_length=1000)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Rule(models.Model):
    rule_name = models.CharField(max_length=1000)
    campaigns = models.ForeignKey(
        'Campaign', on_delete=models.CASCADE)
    schedule = models.TimeField()
    condition = models.TextField()
    Activate = 'Activate'
    Deactivate = 'Deactivate'
    STATUS_CHOICES = (
        (Activate, 'Activate'),
        (Deactivate, 'Deactivate'),
    )
    STATUS = models.CharField(
        max_length=1000,
        choices=STATUS_CHOICES,
        default=Activate,
    )
    Notify = 'Notify'
    Pause = 'Pause'
    Start = 'Start'
    ACTION_CHOICES = (
        (Notify, 'Notify'),
        (Start, 'Start'),
        (Pause, 'Pause'),
    )
    ACTION = models.CharField(
        max_length=1000,
        choices=ACTION_CHOICES,
        default=Notify)

    def __str__(self):
        return self.rule_name


class VariableMetric(models.Model):
    metric_id = models.CharField(max_length=500)
    rules = models.ForeignKey(
        'Rule', on_delete=models.CASCADE)
    impression = models.IntegerField(blank=True, null=True)
    click = models.IntegerField(blank=True, null=True)
    install = models.IntegerField(blank=True, null=True)
    spend = models.IntegerField(blank=True, null=True)
    ecpm = models.IntegerField(blank=True, null=True)
    ecpi = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.metric_id
