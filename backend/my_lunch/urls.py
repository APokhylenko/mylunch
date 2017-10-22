from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

import rest_framework_jwt.views
import djoser.views

urlpatterns = [
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^api/v1/', include('order.urls', namespace='orders')),
                  url(r'^auth/login', rest_framework_jwt.views.obtain_jwt_token),  # using JSON web token
                  url(r'^auth/refresh', rest_framework_jwt.views.refresh_jwt_token),
                  url(r'^auth/register', djoser.views.RegistrationView.as_view()),
                  url(r'^auth/password/reset', djoser.views.PasswordResetView.as_view()),
                  url(r'^auth/password/reset/confirm', djoser.views.PasswordResetConfirmView.as_view()),
              ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
