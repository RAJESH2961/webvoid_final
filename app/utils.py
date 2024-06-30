from django.core.mail import send_mail
from django.conf import settings

def send_email_to_user():
    subject ="Testimg mail"
    message ="Hello Welcome !" 
    from_email=settings.EMAIL_HOST_USER
    recipient_list =["grajesh2907@gmail.com"]
    send_mail(subject,message,from_email,recipient_list)