from django.core.mail import send_mail


def send(users_email, text, header):
    send_mail(header,
    text,
    "speedbeast200@gmail.com",    
    users_email)