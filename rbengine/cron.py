from django.conf import settings
from .models import Rule, Campaign, VariableMetric
from django.core.mail import send_mail


def notify(user_list):
    '''Notify action that takes in user email as argument'''
    subject = 'Promotial:Rule conditions exceeded'
    meassage = 'Hey ! /n The rule that you set have exceeded the condition that you specified.'
    from_email = settings.EMAIL_HOST_USER
    to_list = []
    to_list.append(user_list)
    send_mail(subject, meassage, from_email, to_list)


# cron job
def my_scheduled_job():
    a = Rule.objects.filter(STATUS='Activate').values_list(
        "schedule", flat=True)
    print(a)
