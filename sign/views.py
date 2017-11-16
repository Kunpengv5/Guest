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
            response = HttpResponseRedirect('/event_manage/')
           # response.set_cookie('user',username,3600)  #添加浏览器cookie
            request.session['user'] = username  #将session信息记录到浏览器
            return response
            # return HttpResponseRedirect('/event_manage/')
        else:
            return render(request,'index.html',{'error':'username or password error!'})

def event_manage(request):
   # username = request.COOKIES.get('user','') #读取浏览器cookie
    username = request.session.get('user','') #读取浏览器的session
    return render(request,"event_manage.html",{"user":username})
