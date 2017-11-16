from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   # return HttpResponse("Hello Django!")
     return render(request,"index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        passwd = request.POST.get('password','')
        if username == 'admin' and passwd == 'admin123':
            return HttpResponse('login success')
        else:
            return render(request,'index.html',{'error':'username or password error!'})
