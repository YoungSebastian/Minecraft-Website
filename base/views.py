from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from .models import messageModel, FormWithCaptcha

import yagmail

topics = {
        'payment':  'Płatność',
        'server':   'Usprawnienie servera.',
        'rofl':     'Admin daj moda.',
        'other':    'Inne.',
    }

def send_email(emailTo,name,emailFrom,topic,message):

    message = f"<h1>McUtopia.fun - SERVER</h1><h2>Temat: {topic}</h2><h3>Od {name}, {emailFrom}</h3><p>{message}</p>"
    yag = yagmail.SMTP(user='', password='')

    yag.send(to=emailTo, subject=topic, contents=message)
    print("Email sent successfully")

def home(request):
    return render(request,'base/home.html')

def contact(request):

    if request.method == 'POST':

        name    = request.POST.get('name')
        email   = request.POST.get('email')
        topic   = request.POST.get('topic')
        message = request.POST.get('message')
        
        Form = FormWithCaptcha(request.POST)
        if (email and topic and message) is not None and Form.is_valid():
            topic = topics.get(topic,"Nieprawidłowy temat.")

            print(name, email,topic,message)
            x = messageModel(name=name,email=email,topic=topic,message=message)
            x.save()

            send_email('',name,email,topic,message)
            return redirect(home)
    
    return render(request,'base/contact.html',{'captcha': FormWithCaptcha})
