from django.shortcuts import render, get_object_or_404

from .models import Member


# Create your views here.
def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def members(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'members.html', context)

def member_detail(request, id):
    member = get_object_or_404(Member, id=id)
    context = {'member': member}
    return render(request, 'member_detail.html', context)