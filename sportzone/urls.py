from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("HELLO TEST 123")
def home(request):
    return render(request, "index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]