from django.urls import path

from users import views

urlpatterns = [
    path('login/', views.Login.as_view()),
    path('logout/', views.logout),
    path('is_authenticated/', views.is_authenticated),
    path('notification/', views.send_notification),
    path('notification/user/', views.send_notification_user),
    path('profile/update/', views.update_user),
    path('register/create/', views.create_user),
    path('profile/info/', views.get_info_user),
    path('block/', views.block_user),
]
