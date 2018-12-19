from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from django.conf import settings


@csrf_protect
def homepage(request):
    if request.method == "POST":
        print(request.POST)
        x = str(request.POST.get('email'))
        print(x)
        subject = 'Django, DO not reply'
        from_email = settings.EMAIL_HOST_USER
        from_email1 = [ settings.EMAIL_HOST_USER ]
        to_email = [x]
        message = " Welcome, and test worked ^.^ , this email has been sent from : " \
                  + from_email + \
                  " because this is an email that this website is currently using, your " \
                  "password is : " + request.POST.get('password')
        message1 = " Message has been sent "

        send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=message, fail_silently=False)
        send_mail(subject=subject, from_email=from_email, recipient_list=from_email1, message=message1, fail_silently=False)

    return render(request, "home.html")


def whopage(request):
    return render(request, "WhoAmI.html")


def projectspage(request):
    return render(request, "MyProjects.html")


def Skillzpage(request):
    return render(request, "AllSkills.html")

