import random
from django.core.mail import EmailMessage
from .models import CustomUser, OneTimePassword
from django.conf import settings


def generateOtp():
    otp = ""
    for i in range(6):
        otp += str(random.randint(1,9))
    return otp


def send_code_to_user(email):
    Subject = "One time passcode for Email verification"
    otp_code = generateOtp()
    print(otp_code)
    user = CustomUser.objects.get(email=email)
    current_site = "ResumeWonder.com"
    email_body = f"Hi {user.first_name}, \nThanks for signing up on {current_site}. \nVerify your email with the one time passcode {otp_code}"
    from_email = settings.FROM_DEFAULT_EMAIL

    OneTimePassword.objects.create(user=user, code=otp_code)

    d_email = EmailMessage(subject=Subject, body=email_body, from_email=from_email, to=[email])

    d_email.send(fail_silently=True)


def send_normal_email(data):
    email = EmailMessage(
        subject=data["email_subject"], 
        body=data["email_body"], 
        from_email=settings.EMAIL_HOST_USER, 
        to=[data["to_email"]]
    )
    email.send()