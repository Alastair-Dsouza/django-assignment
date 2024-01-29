from .models import User
import time
from django.core.mail import send_mail
from django.conf import settings

def send_email_to_client():
    subject = "This is Django Test Message Subject"
    message = "This is Django Test Message Text"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["dsouzaalastair19092002@gmail.com"]

    send_mail(subject,message,from_email,recipient_list)