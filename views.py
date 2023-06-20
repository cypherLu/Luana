from turtle import title
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import fanfic
from .forms import fanficForm
from django.contrib import messages

def kilig(request):
        search = request.GET.get('search')
        if search:
            fanfics = fanfic.objects.filter(title__icontains=search)
        else:
          fanfics_list = fanfic.objects.all()
          paginator = Paginator(fanfics_list, 1)
          page = request.GET.get('page')
          fanfics = paginator.get_page(page)
        return render(request, 'kilig.html', {'fanfics': fanfics})

def fanficView(request, id):
    Fanfic = get_object_or_404(fanfic, pk=id)
    return render(request, 'fanfic.html', {'fanfic': Fanfic})

def newFanfic(request):
    if request.method == 'POST':
      form = fanficForm(request.POST)
      if form.is_valid():
        Fanfic = form.save()
        return redirect('/')

    else:
      form = fanficForm()
    return render(request, 'addfanfic.html', {'form': form})

def editfanfic(request, id):
    Fanfic = get_object_or_404(fanfic, pk=id)
    form = fanficForm(instance=Fanfic)
    if (request.method == 'POST'):
        form = fanficForm(request.POST, instance=Fanfic)
        if(form.is_valid()):
            Fanfic.save()
            return redirect('/')
        else:
                return render(request, 'editfanfic.html', {'form': form, 'Fanfic': Fanfic})
    else:
     return render(request, 'editfanfic.html', {'form': form, 'Fanfic': Fanfic})

def deletefanfic(request, id):
    Fanfic = get_object_or_404(fanfic, pk=id)
    Fanfic.delete()
    messages.info(request, 'fanfic deleted successfully!')
    return redirect('/')