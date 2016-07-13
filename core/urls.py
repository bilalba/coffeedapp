from django.conf.urls import url, patterns
from django.contrib import admin
import core.views as coreviews

urlpatterns = [
    url(r'^$', coreviews.LandingView.as_view()),
]
 