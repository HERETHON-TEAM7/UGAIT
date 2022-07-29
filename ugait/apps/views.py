from django.shortcuts import render, redirect
from django.db import models
from django.shortcuts import *
from .models import *
from forms import *
# Create your views here.


def findaguideview(request):
    location = User.location
    if location == 'seoul':
        tourtheme1 = request.POST['tourtheme']
        if tourtheme1 == Guide.tourtheme:
            return render('match.html')


def guidematchedview(request):
    return render('match_success.html')