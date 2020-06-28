from django.shortcuts import render
from django.http import HttpResponse
from base.models import FormWithCaptcha
from .models import paymentModel

import yagmail

products = [
    'vip','sponsor','kozak'
]


def send_email(emailTo,name,emailFrom,topic,message,product):

    message = f"<h1>McUtopia.fun - SERVER</h1><h2>Temat: {topic} </h2><h3>Nazwa Minecraft - {name}</h3><h3>Email - {emailFrom}</h3><h3>Produkt - {product}</h3><p>{message}</p>"
    yag = yagmail.SMTP(user='', password='')

    yag.send(to=emailTo, subject=topic, contents=message)
    print("Email sent successfully")

def home(request):
    return render(request,'shop/home.html')

def payment(request,product):
    if product in products:
        if request.method == 'POST':

            name    = request.POST.get('name')
            email   = request.POST.get('email')
            message = request.POST.get('message')
            
            Form = FormWithCaptcha(request.POST)
            if (email and name) is not None and Form.is_valid():
                
                x = paymentModel(name=name,email=email,message=message)
                x.save()

                topic = 'Zamówienie #' + str(x.pk) 
                print(name, email,topic,message)

                send_email('',name,email,topic,message,product)

                context = {
                    'payment_number': topic
                }
                
                return render(request,'shop/payment_succes.html',context)
            else:
                return HttpResponse("Coś poszło nie tak, spróbuj ponownie")
        else:
            return render(request,'shop/payment.html',{'product':product,'captcha': FormWithCaptcha})
    else:
        return HttpResponse("Nie mamy takiego produktu ?")