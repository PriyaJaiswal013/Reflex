from .models import *
from django.core.mail.message import EmailMultiAlternatives
from django.core.mail import get_connection
from accounts.models import *
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, message
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.core.mail.backends.smtp import EmailBackend
from random import randint 

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

import random
import string

def get_random_string(n):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(n))
    print("Random string of length", n, "is:", result_str)
    
    return result_str

# get_random_string(8)
# get_random_string(6)
# get_random_string(4)

# def account_activation():
#     to_email = []
#     order = Order.objects.get(id=orderID)
#     order.confirmDelivery()
#     order.save()
#     mail_subject = 'Order Delivered successfully'
#     to = str(order.customer.customer.email)
#     to_email.append(to)
#     from_email = 'craftinimages1@gmail.com'
#     message = "Hi "+order.customer.customer.first_name+" Your order was delivered successfully. Please go to your dashboard to see your order history. <br> Your order id is "+orderID+". Share your feedback with us."
#     send_mail(
#         mail_subject,
#         message,
#         from_email,
#         to_email,
#     )
#     return redirect('hotel:orders_admin')

# def send_mail(subject, message, from_email, to_email, html_message=None):
#     connection = email_connection(from_email)
#     mail = EmailMultiAlternatives(subject, message, from_email, to_email, connection=connection)                            
#     if html_message:
#         mail.attach_alternative(html_message, 'text/html')
#     return mail.send()

# def email_connection(from_email): 
#     email_host = 'smtp.gmail.com'
#     auth_user =  'craftinimages1@gmail.com'  # 'kambiwebtest@gmail.com'
#     auth_password = 'Pr1y@123' # 'kambiweb@12345'
#     port =  587
#     # use_tls = True  
#     connection = get_connection(host=email_host, username=auth_user, password=auth_password,
#                 fail_silently=False, port=port, use_ssl=False, use_tls=True)
#     return connection