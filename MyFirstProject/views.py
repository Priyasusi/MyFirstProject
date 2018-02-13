from django.http import HttpResponse
from django.shortcuts import render
def home_page(request):
    home="priya"
    return render(request,"home_page.html",{})
