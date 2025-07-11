from django.urls import path
from .views import index, about, contact, members, member_detail

app_name = 'members'

urlpatterns = [
    path('', index,name='index'),
    path('about/', about,name='about'),
    path('contact/', contact,name='contact'),
    path('members/', members,name='members'),
    path('members/<int:id>', member_detail,name='detail'),
]