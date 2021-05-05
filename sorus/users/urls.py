from django.urls import path

from users.views import Login, logout, send_notification, send_notification_user

urlpatterns = [
    path('login/', Login.as_view()),
    path('logout/', logout),
    path('notification/', send_notification),
    path('notification/user/', send_notification_user),
]