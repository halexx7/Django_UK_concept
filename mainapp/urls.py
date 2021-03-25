from django.conf import settings
from django.urls import path, include
from django.views.generic.base import TemplateView
from invoice import views

urlpatterns = [
    path('invoice/', views.main, name='invoice'),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()