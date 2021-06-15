from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^profile/$', accounts, name='accounts'),
    # url(r'^accounts/companydetails/$', companydetails, name='companydetails'),
    url(r'^accounts/change/password/$', changepassword, name='changepassword'),
    url(r'^accounts/forgot/password/$', forgotpassword, name='forgotpassword'),
    # url(r'^accounts/register/site/$', site_registration, name='site-register'),
    url(r'^accounts/login/$', login_site, name='signin'),
    url(r'^accounts/signup/$', signup, name='signup'),
    url(r'^accounts/cust_signup/$', cust_signup, name='cust_signup'),
    # url(r'accounts/signin/(?P<username>.+)/$', admin_login, name='admin_login'),
    # url(r'^accounts/verifysite/(?P<slug>.+)/$', site_verification, name='site-verification'),
    url(r'^accounts/logout/$', auth_logout, name='auth-logout'),

    #url(r'mysite/settings/private-ips/$', settings_private_ips, name="settings-private-ips"),
    # url(r'mysite/settings/associate-domain-ip/(?P<slug>.+)/$', settings_associate_domain_ip, name="settings-associate-domain-ip"),
    # url(r'mysite/settings/allocate-private-ip/$', allocate_private_ips, name="allocate-private-ips"),
    # url(r'mysite/settings/change-ip-status/(?P<ip>.+)/(?P<status>\d+)/$', change_ip_status, name="change_ip_status"),
    # url(r'mysite/accounts/usage/$', accounts_usage, name="accounts_usage"),
    # url(r'^mysite/api/$', ApiKey, name='Api'),
    # url(r'^mysite/subuser/$', subuser, name='subuser'),
    # url(r'^mysite/subuser/add/$', change_subuser, name='add'),
    # url(r'^mysite/subuser/subuser_detail/(?P<slug>.+)/$', subuser_details, name='subuser_detail'),
    # url(r'^mysite/subuser/edit_subuser/(?P<slug>.+)/$', edit_subuser, name='edit_subuser'),
    # url(r'^mysite/subuser/delete_subuser/(?P<slug>.+)/$', delete_subuser, name='delete_subuser'),
    # url(r'^mysite/api/action/(?P<status>.+)/$', api_access, name="api_access"),
    #url(r'^mysite/api/$', TemplateView.as_view(template_name='myadmin/my_api_credentials.html'), name="api_details"),


]

