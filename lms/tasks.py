import datetime

from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from users.models import User
from datetime import datetime, timedelta


@shared_task
def send_email(user_email):
    subject = 'Обновление курса'
    message = 'Ваш курс обновлен'
    send_mail(subject, message, EMAIL_HOST_USER, user_email)


@shared_task
def deactivate_user_afk():
    users = User.objects.all()
    today = datetime.today()
    for user in users:
        time_difference = today - user.last_login
        if time_difference > timedelta(days=30):
            user.is_active = False
            user.save()


