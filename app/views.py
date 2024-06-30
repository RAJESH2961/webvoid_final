from django.shortcuts import render,redirect
from .models import*
from webvoid import settings
from django.core.mail import EmailMessage

# Create your views here.
def home(req):
    return render(req,'index.html')


def contact(req):
    if req.method=="POST":
        name = req.POST['name']
        email = req.POST['email']
        number = req.POST['mobile']
        subject = req.POST['subject']
        message = req.POST['message']
        user=ContactForm(name=name, email=email, mobile=number, subject=subject, message=message)
        user.save()
        sub="Thank you for contacting us,f'"
        body="Hi {name},Thank you for reaching out! We have received your message and will get back to you shortly.\n\nBest regards,\n"
        sender=settings.EMAIL_HOST_USER
        receiver=email
        email_msg=EmailMessage(sub,body,sender,[receiver])
        return redirect('success')
    else:
        return render(req,'contact/contactus.html')

def success(req):
    return render(req,'contact/success.html')

def aboutus(req):
    return render(req,'about_us.html')

def services(req):
    return render(req,'services.html')

def data(request):
    # services_list = Services.objects.filter(status=0)
    services_list = Services.objects.all()
    return render(request, 'data.html', {'services_list': services_list})
def data_view(req,id):
    service_detail_list = Service_detail.objects.filter(name=id)
    return render(req, "data_details.html",{"data": service_detail_list})

def test(req):
    data1 = ContactForm.objects.values_list('email', flat=True)
    # data_final={
    #     "data" : data1
    # }
    # final_date=data.objects.filter(name = 'Rajesh') 
    return render(req,'test.html', {"data":data1})

