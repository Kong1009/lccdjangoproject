from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
import requests


def contactform(request):
    if request.method == "POST":
        # 迭代所有 POST 數據
        for key, value in request.POST.items():
            print(f"{key}: {value}")
            
            
        # 提取 reCAPTCHA 響應令牌
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = "https://www.google.com/recaptcha/api/siteverify"
        
        # 密鑰
        secret_key = '6LdMlvkpAAAAAEGdGzgi5Egr_s0DHiCdhL5IY4EZ'

        # 構建驗證請求的數據
        data = {
            'secret': secret_key,
            'response': recaptcha_response
        }

        # 發送請求到 Google 的 reCAPTCHA 驗證 API
        response = requests.post(url, data=data)
        result = response.json()

        if result.get("success"):
        
            email = request.POST.get("email")
            purpose = request.POST.get("purpose")
            content = request.POST.get("content")
            
            data = Contact(
                    email = email,
                    purpose = purpose,
                    content = content
                )
            
            data.save()
            messages.success(request, "您的問題已收到，請等待回覆")
        else:
            messages.error(request, "驗證失敗，請重新嘗試")
        
        return redirect('contact')
    
    return render(request, 'contact.html')



def about(request):
    return render(request, "about.html")

def test(request):
    return render(request, "test.html")