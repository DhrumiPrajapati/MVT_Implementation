from django.shortcuts import render, HttpResponseRedirect
from .forms import EmpRegistration
from .models import User

# Create your views here.

#this fun will add and show new items
def add_show(request):
    if request.method == 'POST':
        fm = EmpRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = EmpRegistration()
    else:
        fm = EmpRegistration()
    emp = User.objects.all()
    return render(request, 'App/addandshow.html', {'form':fm, 'ep':emp})

#this fun will edit or update
def update_data(request, id):
    if request.method == 'POST' :
        pi = User.objects.get(pk=id)
        fm = EmpRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = EmpRegistration(instance=pi)
    return render(request, 'App/update.html', {'form':fm})

#this fun will delete items
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')