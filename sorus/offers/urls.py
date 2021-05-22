from django.urls import path

from offers import views

urlpatterns = [
    path('review/create/', views.create_review),
    path('product/register/', views.create_offer),
    path('product/list/', views.list_offers),
    path('product/query/', views.search_offers),
    path('product/user_list/', views.list_user_offers),
    path('product/update/', views.update_product),
]
