from django.core.checks import messages
from django.core.management.base import BaseCommand, CommandError
from accounts.models import *
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, message
from django.core.mail import send_mail
from django.conf import settings
from accounts.utils import *  
from django.core.mail.message import EmailMultiAlternatives
from django.core.mail import get_connection
from django.core import mail
from django.core.mail.backends.smtp import EmailBackend


class Command(BaseCommand):
    help = 'Send Email'

    def handle(self, *args, **options):
        userprofile = UserProfile.objects.filter(login_as=0, status=1)
        print(userprofile)
        # user = User.objects.filter()
        
        for userprofile in userprofile:
            password = str(random_with_N_digits(5))
            # password = get_random_string(8)
            to_email = userprofile.user.email
            mess = f"Hello Congratulations {userprofile.firstname},\nYour username is {userprofile.user.username},\nYour Password is {password}\nThanks!"
            print(mess)

            if userprofile:
                send_mail(
                        subject="Welcome to Craftin` Images`  - Approved Your Account",
                        message=mess,
                        from_email = settings.EMAIL_HOST_USER,
                        recipient_list = [to_email],
                        fail_silently = False
                        )
                userpro = UserProfile.objects.update(status=2)
                new_user, created = User.objects.get_or_create(username=userprofile.user.username, email = userprofile.user.username)
                new_user.set_password(password)
                new_user.save()
        
        
