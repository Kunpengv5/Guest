from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
   # return HttpResponse("Hello Django!")
     return render(request,"index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        passwd = request.POST.get('password','')
        if username == 'admin' and passwd == 'admin123':
            return HttpResponseRedirect('/event_manage/')
        else:
            return render(request,'index.html',{'error':'username or password error!'})

def event_manage(request):
    return render(request,"event_manage.html")
