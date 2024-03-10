from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def viewposts(request):
    return render(request, 'usermodule/viewposts.html')