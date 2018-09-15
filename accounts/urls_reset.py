from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth.views import (password_reset,
                                       password_reset_done,
                                       password_reset_confirm,
                                       password_reset_complete)

''' url patterns for resetting a password '''

urlpatterns = [
    # url to reset a password
    url(r'^$', password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done')},
        name='password_reset'),
    # url for when a reset is done
    url(r'^done/$', password_reset_done, name='password_reset_done'),
    # url for customer to reset password using a unique token for every reset
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')},
        name='password_reset_confirm'),
    # url for when a reset is complete
    url(r'^complete/$', password_reset_complete,
        name='password_reset_complete'),
]
