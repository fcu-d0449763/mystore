from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product_index, name='product_index'),
    url(r'^create$', views.product_create, name='product_create'),
]
