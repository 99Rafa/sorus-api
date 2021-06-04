from django.urls import path

from sales import views

urlpatterns = [
    path('buy_product/', views.buy_product),
    path('buy_subscription/', views.buy_subscription),
]
