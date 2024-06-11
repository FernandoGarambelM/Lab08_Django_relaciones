from django.shortcuts import render, redirect, get_object_or_404
from .models import Destination
from .forms import DestinosTuristicosForm
# Create your views here.

def index(request):
   
    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})

def gestionar_destinos(request, id=None):
    if request.method == 'POST':
        if id:
            destino = get_object_or_404(Destination, id=id)
            form = DestinosTuristicosForm(request.POST, request.FILES, instance=destino)
            if 'modificar' in request.POST:
                if form.is_valid():
                    form.save()
            elif 'eliminar' in request.POST:
                destino.delete()
        else:
            form = DestinosTuristicosForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        return redirect('gestionar_destinos')
    
    else:
        if id:
            destino = get_object_or_404(Destination, id=id)
            form = DestinosTuristicosForm(instance=destino)
        else:
            form = DestinosTuristicosForm()
        
    destinos = Destination.objects.all()
    return render(request, 'gestionar_destinos.html', {
        'form': form,
        'destinos': destinos,
        'id': id,
    })