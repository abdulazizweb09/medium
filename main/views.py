from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import TestForm
# Create your views here.

class HomeView(View):
    def get(self,request):
        if request.user.is_authenticated:
            user=request.user
            post=Test.objects.all()
        
            avatar=None
            if Profile.objects.get(user=user):
                avatar=Profile.objects.get(user=user)

            print(user)
        
            context={
                'user':user,
                'avatar':avatar,
                'post':post,
            }

            return render(request,'home.html',context)
        return redirect('login')
    

class EditView(View):
    def get(self,request):
        form = TestForm()

        return render(request,'create.html',{
            'form': form
        })
    
    def post(self,request):
        user=request.user

        title=request.POST.get('title')
        body = request.POST.get("body")

        Test.objects.create(
            title=title,
            body=body,
            author=user,
        )

        return redirect('/')