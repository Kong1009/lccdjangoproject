from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Contact


def contactform(request):
    if request.method == "POST":
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
        
    return redirect('contact')



def about(request):
    return render(request, "about.html")