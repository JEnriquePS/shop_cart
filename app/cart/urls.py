from django.conf.urls import url
from .views import compra
urlpatterns = [
    url(r'^compra/$', compra, name='compra'),

]
