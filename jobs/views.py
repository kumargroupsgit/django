from django.shortcuts import render
from .models import Job
# Create your views here.

def home(requst):
    jobs = Job.objects
    return render(requst, 'jobs/home.html', {'jobs':jobs})