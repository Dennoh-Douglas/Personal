from django.shortcuts import render
from .models import Student

# Create your views here.

def add(request):
    return render(request,'add.html')


def insert_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        adm_no = request.POST.get('adm_no')
        email = request.POST.get('email')
        image = request.FILES['image']

        student = Student(name=name, age=age, adm_no=adm_no, email=email, image=image)
        student.save()

    return render(request, 'add.html')


def view_data(request):
    students = Student.objects.all()
    return render(request, 'view_data.html', {'students':students})

