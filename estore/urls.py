from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product_index, name='product_index'),
    url(r'^new', views.product_new, name='product_new'),
]
