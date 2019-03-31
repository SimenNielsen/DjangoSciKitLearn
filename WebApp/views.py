from django.shortcuts import render
from .rock_paper_scissors import *

# Create your views here.

def index(request):
    generate_model()
    #test()
    return render(request, 'index.html')