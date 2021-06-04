from django.urls import path

from offers import views

urlpatterns = [
    path('review/create/', views.create_review),
    path('product/register/', views.create_offer),
    path('product/list/', views.list_offers),
    path('product/categories/', views.get_categories),
    path('product/user_list/', views.list_user_offers),
    path('product/update/', views.update_product),
    path('product/list_top/', views.list_top_offers),
]
