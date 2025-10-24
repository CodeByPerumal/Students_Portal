from django.shortcuts import render
from portal.models import Students

def home_page(request):
    students = Students.objects.all()
    return render(request, 'home.html', {'students': students})