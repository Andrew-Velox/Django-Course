from django.shortcuts import render
from datetime import datetime,timedelta
from django.http import HttpResponse
# Create your views here.

def home(request):
    response = render(request,'home.html')
    response.set_cookie("name","Andrew")
    # response.set_cookie("name","Velox", max_age=60*3)
    response.set_cookie("name","Velox", expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookie.html',{'name':name})

def delete_cookie(request):
    response = render(request,'del_cookie.html')
    response.delete_cookie('name')
    return response
    

def set_session(request):
    # data = {
    #     'name' : "Rahim",
    #     'age' : 29,
    #     'language' : 'bangla'
    # }
    # print(request.session.get_session_cookie_age())
    # print(request.session.get_expiry_date())
    # request.session.update(data)
    request.session['name']="Andrew Velox"
    return render(request,'home.html')


def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name','Guest')
        age = request.session.get('age')
        # print(name)
        request.session.modified = True
        return render(request, 'get_session.html',{'name':name, 'age':age})
    else:
        return HttpResponse('Your Session has been expired')

def delete_session(request):
    # del request.session['name']

    request.session.flush()
    request.session.clear_expired()
    return render(request,'del_cookie.html')