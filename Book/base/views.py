
from multiprocessing import context
from django.shortcuts import render
from  django.http import HttpResponse
from . models import Data
from django.db.models import Q

# Create your views here.
def home(request):
    if 'q' in request.GET:
        q= request.GET['q']
       # data= Data.objects.filter(first_name__icontains=q)

        multiple_q = Q(Q(first_name__icontains=q)| Q(last_name__icontains=q))
        data= Data.objects.filter(multiple_q)

        
    else:
              data =Data.objects.all()

    context ={
        'data': data
    }

    return render(request, 'home.html', context)


def nav(request):
    return render(request, 'Blogs/nav.html')

def base(request):
    return render(request, 'Blogs/base.html') 