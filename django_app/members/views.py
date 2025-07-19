from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Member


# Create your views here.
def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        messages.success(request, f"{name} ,{email}, {message}")
    return render(request, 'contact.html')

def members(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'members.html', context)

def member_detail(request, id):
    member = get_object_or_404(Member, id=id)
    context = {'member': member}
    return render(request, 'member_detail.html', context)

def process_get_form_request(request):
    username = request.GET.get('username')
    email = request.GET.get('email')
    message = request.GET.get('message')
    gender = request.GET.get('gender')
    context = {'username': username, 'email': email, 'message': message, 'gender': gender}
    return render(request, 'task_class_view/process_get_form.html', context)

def category_selection_form(request):
    choice = request.GET.get('category')
    return render(request, 'task_class_view/category_selection_form.html', {'choice': choice})

def submit_feedback(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        username = request.POST.get('username')
        print(feedback, username)
        messages.success(request, f"hello {username} your message was send ,{feedback}")
        return redirect('members:submit_feedback')
    elif request.method == 'GET':
        return render(request, 'task_class_view/submit_feedback.html')