from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from QandA.models import Userqa 

# 계정 관리

def signup(request):
    if request.method == 'POST':
        if len(request.POST['username']) < int(8) or len(request.POST['username']) > int(15):
            return render(request, 'signup.html', {'error': '아이디는 8글자 이상/ 15글자 미만으로 하세요'})
        
        elif request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': '해당 아이디가 이미 존재합니다'})
            except:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('index')
        
        else:
            return render(request, 'signup.html', {'error': '비밀번호를 동일하게 입력하세요'})
    
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('user_page')
        else:
            return render(request, 'login.html', {'error': '아이디 또는 비밀번호가 올바르지 않습니다'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    return render(request, 'index.html')

# 유저 페이지 관리

def user_page(request):
    logined = request.user   # login한 User
    logined_user = logined.username
    user_qa = Userqa.objects.filter( reader = logined_user )[:3]
    user_qa_view = Userqa.objects.filter( reader = logined_user )
    n = user_qa_view.count()
    return render(request, 'user_page.html', {
        'userqas' : user_qa,
        'n' : n,
    })