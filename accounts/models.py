from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)



LOGIN_AS = ((0, 'RESTAURANT OWNER '), (1, 'CUSTOMER'))
STATUS = ((0, 'PENDING '), (1, 'TO_BE_VERIFY'), (2, 'APPROVED'))

# Create your models here.
class UserProfile(models.Model):
    # pending = 'Pending'
    # verified = 'Verified'

    # STATUS = (
    #     (pending,pending),
    #     (verified,verified),
    # )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userdetail")
    firstname = models.CharField(max_length = 100, null=True, blank=True)
    lastname = models.CharField(max_length = 100, null=True, blank=True)
    address_first = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    mobile = models.CharField(max_length = 100, null=True, blank=True)
    orders = models.IntegerField(default=0)
    total_sale = models.IntegerField(default=0)
    status = models.IntegerField(choices = STATUS, default=0)
    restaurant_name = models.CharField(max_length = 100, null=True, blank=True)
    serving_type_food = models.CharField(max_length = 100, null=True, blank=True)
    city = models.CharField(max_length = 100, null=True, blank=True)
    fssai_number = models.CharField(max_length = 100, null=True, blank=True)
    pin_code = models.CharField(max_length = 100, null=True, blank=True)
    landmark = models.CharField(max_length = 100, null=True, blank=True)
    login_as = models.IntegerField(choices = LOGIN_AS, null=True, blank=True)


    def __str__(self):
        return str(self.user.username)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



class Restaurants(AbstractBaseUser):
    username = models.CharField(max_length = 50, null=False)
    email = models.EmailField(max_length=254)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    address_first = models.TextField()
    address = models.TextField()
    restaurant_latitude = models.FloatField(null=True)
    restaurant_longitude = models.FloatField(null=True)
    mobile = models.IntegerField()
    orders = models.IntegerField(default=0)
    total_sale = models.IntegerField(default=0)
    status = models.IntegerField(choices = STATUS, default=0)
    restaurant_name = models.CharField(max_length = 100)
    serving_type_food = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    fssai_number = models.CharField(max_length = 100)
    pin_code = models.CharField(max_length = 100)
    landmark = models.CharField(max_length = 100)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class Customers(AbstractBaseUser):
    username = models.CharField(max_length = 50, null=False)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    email = models.EmailField(max_length=254)
    mobile = models.IntegerField()

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active