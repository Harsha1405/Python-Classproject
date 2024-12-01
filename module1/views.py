from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
import random,string


def hello1(request):
    return HttpResponse('<center> Welcome to TTM Homepage</center>')
# Create your views here.

def newhomepage(request):
    return render(request,'newhomepage.html')


def travelpackage(request):
    return render(request, 'travelpackage.html')


def print1(request):
    return render(request,'print_to_console.html')


def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
    a1 = {'user_input':user_input}
    return render(request,'print_to_console.html',a1)


def randomcall(request):
    return render(request,'randomotpgenerator.html')


def randomlogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
        a2 = int(user_input)
        ran1 = ''.join(random.sample(string.digits, k=a2))
    a1 = {'ran1':ran1}
    return render(request,'randomotpgenerator.html',a1)


def getdate1(request):
    return render(request, 'get_date.html')

from .forms import *
import datetime
from django.shortcuts import render
def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request,'get_date.html',{'updated_date':updated_date})
        else:
            form = IntegerDateForm()
        return render(request,'get_date.html',{'form': form})

def registerlogin(request):
    return render(request, 'RegisterForm.html')


from .models import*
from django.shortcuts import render,redirect
def registerloginfunction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        if Register.objects.filter(email=email).exists():
            return HttpResponse('Email already registered. Choose a different email.')
        Register.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request,'RegisterForm.html')


def pie(request):
    return render(request, 'chart_form.html')


import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})


def travelservices(request):
    return render(request, 'travelservices.html')

import requests

def weatherpagecall(request):
    return render(request,'weatherappinput.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = ''
        url = ''
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature-273.15 , 2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})




def feedback(request):
    return render(request,'feedbackform.html')


def feedbackfunction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        feedback_text = request.POST.get('feedback_text')
        tosend=feedback_text+"Thank You"
        if Feedback.objects.filter(email=email).exists():
            return HttpResponse('Email already registered. Choose a different email.')

        Feedback.objects.create(name=name,email=email, phonenumber=phonenumber,feedback_text=feedback_text)
        send_mail(
            "Thank you for contacting harsha travels",
            tosend,
            '',
            [email],
            fail_silently=False,
        )
        return redirect('newhomepage')

    return render(request, 'feedbackform.html')


def signup1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password1')

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists.')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account Created Successfully!')
                return render(request, 'newhomepage.html')
        else:
            messages.info(request, 'Passwords do not match')
            return render(request, 'signup.html')
    else:
        # Handle GET request (display the signup form)
        return render(request, 'signup.html')

def login(request):
    return render(request,'login.html')

from django.shortcuts import redirect

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(request, username=username, password=pass1)

        if user is not None:
            auth.login(request, user)
            return redirect('newhomepage')  # Replace with the actual view name or URL pattern
        else:
            messages.info(request, 'Invalid Credentials.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'newhomepage.html')
def signup(request):
    return render(request,'signup.html')
