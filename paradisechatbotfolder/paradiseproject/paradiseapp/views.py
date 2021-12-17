from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from paradiseapp.models import Chatbot
from .forms import ChatbotForm


def index(request):

    chatbot=Chatbot.objects.all()
    context={
        'chatbot':chatbot
    }

    return render(request,"index.html",context)

def detail (request,chatbot_id):

    chatbot=Chatbot.objects.get(id=chatbot_id)
    return render(request,"detail.html",{'chatbot':chatbot})

def addchatbot(request):


    if request.method=="POST":

        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        chatbot=Chatbot(name=name,desc=desc,year=year,img=img)
        chatbot.save()


    return render(request,"addchatbot.html")


def update(request,id):
    chatbot=Chatbot.objects.get(id=id)
    form=ChatbotForm(request.POST or None,request.FILES,instance=chatbot)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'chatbot':chatbot})


def delete(request,id):

    if request.method=="POST":


        chatbot=Chatbot.objects.get(id=id)
        chatbot.delete()
        return redirect('/')
    return render(request,'delete.html')



