from django.urls import path

from users.views import Login, logout

urlpatterns = [
    path('login/', Login.as_view()),
    path('logout/', logout)
]
