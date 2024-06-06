from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Members
import hashlib

myapp = "myapp"
# Create your views here.
def createMember(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        checkpassword = request.POST.get("checkpassword")

        
        form_data = {
            'username': username,
            'userEmail': email,
        }
        
        # 前端檢查密碼的部分暫時先跳過
        if password == checkpassword:        
            objects = Members.objects.filter(userEmail = email).exists()
            
        
            if objects:
                msg = email+"已存在"
            else:
                
                password = hashlib.sha3_256(password.encode(encoding='utf-8')).hexdigest()
                member = Members(
                    username = username,
                    userEmail = email,
                    userPassword = password
                    )
                
                member.save()
                msg = "恭喜您已註冊完成"
        else:
            msg = "請確認密碼是否一致!!!!"
    return render(request, "register.html", {"msg": msg, "form_data": form_data})

def checklogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        remember_account = request.POST.get('inputRememberEmail')
        password = hashlib.sha3_256(password.encode(encoding='utf-8')).hexdigest()

        try:
            member = Members.objects.get(userEmail = email)
        except:
            messages.error(request, "帳號未註冊")
            return redirect("login")
        
        
        if member.userPassword != password:
            messages.error(request, "密碼錯誤，請重新輸入")
            return redirect("login")
        
        
        # response = redirect("myapp:home")
        response = redirect("myapp:home")

        if remember_account:
            response.set_cookie("remember_account", email, max_age=3600)
        request.session["user_email"] = email

        return response
            
def logout(request):
    if "user_email" in request.session:
        del request.session["user_email"]
        messages.success(request, "您已登出~~~~~~~~~~~~~~")        
    else:
        messages.warning(request, "您尚未登录。")
        
    return redirect("myapp:home")


def test(request):
    
    response = HttpResponse("OK")
    response.set_cookie("remembser_account", "testcookie", max_age=3600)
    return response