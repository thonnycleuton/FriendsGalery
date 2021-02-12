from django.conf.urls import url
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from account.views import *

app_name = 'accounts'

urlpatterns = [
    url(r'^$', ProfileList.as_view(), name='list'),
    url(r'^new/$', ProfileCreate.as_view(), name='new'),
    url(r'^update/(?P<pk>\d+)/$', ProfileUpdate.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', ProfileDelete.as_view(), name='delete'),

    url(r'^change-password/$', PasswordChangeView.as_view(success_url=reverse_lazy('contas:perfil'), template_name='account/registration/password_change.html'), name='password_change'),
    url(r'^password_reset/$', PasswordResetView.as_view(email_template_name='registration/password_reset_email.html', template_name='account/registration/password_reset.html', ), name='password_reset'),
    url(r'^password_reset/done/$', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    url(r'^login/$', LoginView.as_view(template_name='account/registration/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]