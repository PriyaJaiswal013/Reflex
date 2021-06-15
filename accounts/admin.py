from django.contrib import admin
from .models import *
# Register your models here.

def make_verified(self, request, queryset):
    queryset.update(status=1)
    # for q in queryset:
    #     q.status=1
    #     q.save()
    #     UserProfile.objects.filter(login_as=q).update(status=1)


make_verified.short_description = "Mark selected stories as Verified"

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'firstname', 'login_as', 'status', 'mobile', 'user_email')
    list_filter = ('mobile', 'status', 'login_as')
    search_fields = ('status', 'login_as')
    list_editable = ('status', )
    ordering = ['status', 'login_as']
    actions = [make_verified]

    def user_email(self, obj):
        return obj.user.email

admin.site.register(UserProfile, UserProfileAdmin)