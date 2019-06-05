from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import RegistrationForm
from .models import RegistrationData
from django.contrib import messages




# Create your views here.

def outlet(request):
    return render(request, "outlet.html")

def karyawan(request):

    return render(request, "Karyawan.html")

def dashboard(request):
    return render(request, "as.html")



def Penentuan(request):
    return render(request, "penentuan_stok.html")

def Laporan(request):

    return render(request, "laporan.html")



def register(request):
    context = {"form":RegistrationForm}


    return render(request, "register.html", context)


def addUser(request):
    form = RegistrationForm(request.POST)


    if form.is_valid():
        register = RegistrationData(Nama_UKM = form.cleaned_data['Nama_UKM'],
                                    Username = form.cleaned_data['Username'],
                                    Password = form.cleaned_data['Password'],
                                    Email = form.cleaned_data['Email'],
                                    No_HP = form.cleaned_data['No_HP'],
                                    Alamat = form.cleaned_data['Alamat'])
        register.save()
        messages.add_message(request, messages.SUCCESS, "You Have Registered Successfully")


    return redirect('add')



def StokBarang(request, operation, pk):
    New_Stok = User.objects.get(pk=pk)
    Stok.make_stok(request.Item, New_Stok)
    return render(request, "stok_barang.html")
