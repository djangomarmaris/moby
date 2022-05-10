from django.shortcuts import render ,redirect
from .models import Social, Product , About ,Personel
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def index(request):
    socials = Social.objects.all()
    products = Product.objects.all()


    context = {
        'socials':socials,
        'products':products
    }
    return render(request,'central/index.html',context)


def about(request):
    socials = Social.objects.all()
    abouts = Personel.objects.all()

    infos = About.objects.all()
    context = {
        'abouts':abouts,
        'infos':infos,
        'socials':socials
    }
    return render(request,'central/about.html',context)



def istec(request):
    socials = Social.objects.all()


    context = {
        'socials':socials
    }
    return render(request,'central/istec.html',context)


def contact(request):
    socials = Social.objects.all()
    if 'btnSubmit' in request.POST:
        if True:
            nerden= 'Moby Marine İletişim Formu'
            name = request.POST.get('name')
            email = request.POST.get('email')
            website = request.POST.get('website')
            comment = request.POST.get('comment')


            subject = 'Moby Marine İletişim Formu'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,"djangomarmaris@gmail.com","info@mobymarine.com.tr"]
            contact_message = "\nNerden:%s\nName:%s\nEmail:%s\nPhone:%s\nSubject:%s" % (
                nerden,
                name,
                email,
            website,
            comment,
            )
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
        return redirect('/')
    return render(request,'central/contact.html',{'socials':socials})