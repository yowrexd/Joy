from django.shortcuts import HttpResponse, render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import PatientForm, CreateProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home_page(request):
    return render(request, "pages/home.html")

def services(request):
    return render(request, "pages/services.html")

def patient(request):
    patientinfo = PatientInfo.objects.all()
    appointment = Appointment.objects.all()
    
    total_patientinfo = patientinfo.count()
    total_appointment = appointment.count()
    
    context = {
        'patientinfo':patientinfo,
        'appointment':appointment,
        'total_patientinfo': total_patientinfo,
        'total_appointment': total_appointment,
        
    }
    return render(request, "pages/patient.html", context)

def patientform(request):
    form = PatientForm()
    context = {'form':form}
    return render(request, 'pages/patientform.html', context)

def about_page(request):
    return render(request, "pages/about.html")

def contact_page(request):
    return render(request, "pages/contact.html")

def nav_bar(request):
    return render(request, "pages/navbar.html")

def footer(request):
    return render(request, "pages/footer.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        patient = authenticate(request, username=username, password=password)
        
        if patient is not None:
            login(request, patient)
            return redirect('home_page')
        else:
            messages.info(request, 'username or password is incorrect')
    return render(request, "pages/login.html")

def signup(request):
    form = CreateProfile()
    context = {'form':form}
    if request.method == 'POST':
        form = CreateProfile(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
            return redirect('login')
            
    return render(request, "pages/signup.html", context)



def form(request):
    form = PatientForm()
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient')
        
    
        
    context = {'form': form}
    return render(request, "pages/form.html", context)


def update(request, pk):
    patients = PatientInfo.objects.get(id=pk)
    form = PatientForm(instance=patients)
    
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patients)
        if form.is_valid():
            form.save()
            return redirect('patient')
    context = {'form': form}
    return render(request, "pages/form.html", context)

def delete(request, pk):
    patients = PatientInfo.objects.get(id=pk)
    if request.method == "POST":
        patients.delete()
        return redirect('patient')
    
    context = {'patients': patients}
    return render(request, "pages/delete.html", context)

