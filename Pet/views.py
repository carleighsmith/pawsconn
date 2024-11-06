from django.shortcuts import render

from django.shortcuts import render
from .models import Pet, SuccessStory, Resource, GetInvolved, SignUp, ContactUs
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AboutForm, ContactForm

def home(request):
    return render(request, 'home.html')

def success(request):
    success_stories = SuccessStory.objects.all()
    return render(request, 'success.html', {'success_stories': success_stories})

def resources_view(request):
    resources = Resource.objects.all()
    
    categorized_resources = {}
    for resource in resources:
        if resource.category not in categorized_resources:
            categorized_resources[resource.category] = []
        categorized_resources[resource.category].append(resource)

    return render(request, 'resources.html', {'categorized_resources': categorized_resources})

def involved(request):
    return render(request, 'involved.html')
def about(request):
    return render(request, 'about.html')

def adopt_view(request):
    pets = Pet.objects.all() 
    return render(request, 'adopt.html', {'pets': pets}) 

def get_involved(request):
    involvement_opportunities = GetInvolved.objects.all()
    return render(request, 'involved.html', {'involvement_opportunities': involvement_opportunities})



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            print(f"Name: {name}, Email: {email}, Message: {message}")
            
            return render(request, 'contact_form.html', {'form': form})
    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form})


def about_form_view(request):
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            return render(request, 'about_form.html', {'form': form})    
        else:
            form = AboutForm()
    
    return render(request, 'about.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import AdoptionForm
from django.contrib import messages

def adoption_form_view(request):
    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            return render(request, 'adoption_form.html', {'form': form})
    else:
        form = AdoptionForm()
        
    return render(request, 'adoption_form.html', {'form': form})

def adoption_success_view(request):
    return render(request, 'adoptsuccess.html')
