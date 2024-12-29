from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request

# Create your views here.


def home(request):
    """ Returns html file with mao page"""
    return render(request, 'catalog/home.html')



def contacts(request):
    """ Return html file. In case in method POST, taking all needed data"""
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f'Data submitted, {name}')

    return render(request, 'catalog/contacts.html')

