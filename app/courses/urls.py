from django.conf.urls import url
from .views import HomeView, add_courses, ListCourses
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='cart'),
    url(r'^add/(?P<id>\d+)/$', add_courses, name='add'),
    url(r'^pago/$', ListCourses.as_view(), name='list_pago'),

]