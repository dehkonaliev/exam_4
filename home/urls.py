from django.urls import path
from .views import home, product_update, product_detail, category, new_product

urlpatterns = [
    path('', home, name='home'),
    path('categories', category, name='categories'),
    path('detail/<int:pk>', product_detail, name='detail'),
    path('update', product_update, name='update'),
    path('new-product', new_product, name='new-product')
]