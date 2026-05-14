from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Rezervace, Trenink

def index(request):
    return render(request, 'sportzone_app/index.html')

@login_required
def vytvorit_rezervaci(request):
    treninky = Trenink.objects.all()
    if request.method == 'POST':
        trenink_id = request.POST.get('trenink')
        datum = request.POST.get('datum')
        cas = request.POST.get('cas')
        Rezervace.objects.create(
            uzivatel=request.user,
            trenink_id=trenink_id,
            datum=datum,
            cas=cas
        )
        return redirect('moje_rezervace')
    return render(request, 'sportzone_app/vytvorit.html', {'treninky': treninky})

@login_required
def moje_rezervace(request):
    rezervace = Rezervace.objects.filter(uzivatel=request.user)
    return render(request, 'sportzone_app/seznam.html', {'rezervace': rezervace})


# Create your views here.
