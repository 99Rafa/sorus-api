from django.urls import path

from users.views import send_notification
from users.views import send_notification_user

urlpatterns = [
    path('notification/', send_notification),
    path('notification/user/', send_notification_user),
]
