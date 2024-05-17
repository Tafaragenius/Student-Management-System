from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import student
from . forms import studentform

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'student':student.objects.all()
        })
    

def view_student(request, id):
    student = student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']
            
            new_student = student(
                student_number=new_student_number,
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                field_of_study=new_field_of_study,
                gpa=new_gpa
            )
            new_student.save()
            return render(request, 'add.html', {
                'form': studentform(),
                'success': True
            })
        else:
            # If form is not valid, render the same form with errors
            return render(request, 'add.html', {
                'form': form
            })
    else:
        # If the request method is not POST, initialize an empty form
        form = studentform()
        return render(request, 'add.html', {
            'form': form
        })
