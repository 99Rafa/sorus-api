from django.urls import path

from offers.views import create_review

urlpatterns = [
    path('review/create/', create_review)
]
