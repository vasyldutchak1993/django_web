from django.shortcuts import render, get_object_or_404
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