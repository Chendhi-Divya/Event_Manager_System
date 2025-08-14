from django.shortcuts import render
from.models import User,Event,Submission

# Create your views here.
def home_page(request):
    users= User.object.filter()
    return render(request,'home.html')