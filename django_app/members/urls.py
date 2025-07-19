from django.urls import path
from .views import index, about, contact, members, member_detail, process_get_form_request, category_selection_form, submit_feedback

app_name = 'members'

urlpatterns = [
    path('', index,name='index'),
    path('about/', about,name='about'),
    path('contact/', contact,name='contact'),
    path('members/', members,name='members'),
    path('members/<int:id>', member_detail,name='detail'),
    path('process_get_form/',process_get_form_request,name='process_get_form'),
    path('category_selection_form/',category_selection_form,name='category_selection_form'),
    path('submit_feedback/',submit_feedback,name='submit_feedback'),
]