from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *

# from .models import Movie

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

# user section
def user_page_view(request):
    return render(request, 'user/user_main_page.html')

def user_dashboard_view(request):
    service_view = Create_Service.objects.all()
    context = {
        'service_view': service_view,
    }
    return render(request, 'user/user_dashboard_page.html', context)

def service_requested_view(request):
    return render(request, 'user/service_requested.html')

def user_profile_view(request):
    return render(request, 'user/user_profile.html')



# service provider section
def service_provider_dashboard_view(request):

    form = Create_ServiceForm()
    if request.method == 'POST':
        form = Create_ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            #this saves the form
            form.save()
            # this refreshes the form
            return redirect('/service_provider_dashboard')

        else:
            print("\n\n\n\n\n\n")
            print(form.errors)
            for i in form:
                print(i.label)
                print(i.errors)
    

    return render(request, 'service_provider/service_provider_page.html', {'form':form} )


def all_services(request):
    display = Create_Service.objects.all()

    form = Create_ServiceForm()
    if request.method == 'POST':
        form = Create_ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            #this saves the form
            form.save()
            # this refreshes the form
            return redirect('/service_provider_dashboard')

        else:
            print("\n\n\n\n\n\n")
            print(form.errors)
            for i in form:
                print(i.label)
                print(i.errors)
    
    context = {
        'display': display,
        'form': form,
    }

    return render(request, 'service_provider/view_services.html', context)

def service_provider_dashboard(request):

    form = Create_ServiceForm()
    if request.method == 'POST':
        form = Create_ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            #this saves the form
            form.save()
            # this refreshes the form
            return redirect('/service_provider_dashboard')

        else:
            print("\n\n\n\n\n\n")
            print(form.errors)
            for i in form:
                print(i.label)
                print(i.errors)
    
    return render(request, 'service_provider/service_provider_dashboard.html', {'form':form})

def user_requests(request):

    form = Create_ServiceForm()
    if request.method == 'POST':
        form = Create_ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            #this saves the form
            form.save()
            # this refreshes the form
            return redirect('/service_provider_dashboard')

        else:
            print("\n\n\n\n\n\n")
            print(form.errors)
            for i in form:
                print(i.label)
                print(i.errors)
    
    return render(request, 'service_provider/user_requests.html',{'form':form})

def service_provider_profile(request):

    form = Create_ServiceForm()
    if request.method == 'POST':
        form = Create_ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            #this saves the form
            form.save()
            # this refreshes the form
            return redirect('/service_provider_dashboard')

        else:
            print("\n\n\n\n\n\n")
            print(form.errors)
            for i in form:
                print(i.label)
                print(i.errors)
    
    return render(request, 'service_provider/service_provider_profile.html', {'form':form})



def update_service_view(request):
    
    form = Create_ServiceForm()
    if request.method == 'POST':
        form = Create_ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            #this saves the form
            form.save()
            # this refreshes the form
            return redirect('/service_provider_dashboard')

        else:
            print("\n\n\n\n\n\n")
            print(form.errors)
            for i in form:
                print(i.label)
                print(i.errors)
    
    
    return render(request, 'service_provider/service_provider_page.html', {'form':form})


def delete_service_view(request, id):
    
    service_created = Create_Service.objects.get(pk=id)
    service_created.delete()
    return render(request,'service_provider/view_services.html')




def user_logout(request):
    logout(request)
    return HttpResponseRedirect('home/index.html')

# # def form_view(request):
#     form = Create_ServiceForm()

#     # form = Create_ServiceForm()
#     if request.method == 'POST':
#         form = Create_ServiceForm(request.POST, request.FILES)
#         if form.is_valid():
#             #this saves the form
#             form.save()
#             # this refreshes the form
#             return redirect('/service_provider_dashboard')

#         else:
#             print("\n\n\n\n\n\n")
#             print(form.errors)
#             for i in form:
#                 print(i.label)

#                 print(i.errors)

#     return render(request, 'service_provider/service_provider_dashboard.html')