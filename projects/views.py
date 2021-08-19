from django.shortcuts import render
from django.http import HttpResponse
from .models import Courses


def index(request):
    courses = Courses.objects
    return render(request, 'projects/index.html', {'courses': courses})
