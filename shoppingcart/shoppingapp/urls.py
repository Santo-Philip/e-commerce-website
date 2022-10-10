from django.urls import path

from . import views

app_name = 'shoppingapp'

urlpatterns = [
    path('', views.allProductCat, name='allProductCat'),
    path('shoppingapp:<slug:c_slug>/', views.allProductCat, name='products_by_category'),
    path('shoppingapp/shoppingapp:<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatDetail'),
]

