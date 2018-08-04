from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib import messages


from .models import employeebiodata
from .forms import employeeForm

# Create your views here.
def index(request):
   return render(request, 'employeebiodata/index.html', {})


def list(request):
    employees = employeebiodata.objects.order_by('dateCreated').all()
    context = {'employees': employees}
    return render(request, 'employeebiodata/list.html', context)


def add(request):
    if request.method == 'POST':
        form = employeeForm(request.POST)
        if form.is_valid():
            employee = employeebiodata(firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],gender=request.POST['gender'],
            email=request.POST['email'])
            employee.save()
            messages.success(request, 'An Employee Record has been added successfully')
            return HttpResponseRedirect('/list/')
    else:
        form = employeeForm()
    return render(request, 'employeebiodata/add.html', {'form': form})
