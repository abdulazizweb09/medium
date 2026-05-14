from django.shortcuts import render
from django.views import *
from main.models import Profile
# Create your views here.

class LoginView(View):
    def get(self,request):
        return render(request, "login.html")

class ProfileView(View):
    def get(self,request,name):
        user=request.user
        profile=ProfileView(user=user)
        social = user.socialaccount_set.filter(provider='google').first()

        avatar = Profile.objects.get(user=user).avatar
        print(profile)

        context={
            'name':user,
            'profile':profile,
            'avatar':avatar,
        }

        return render(request,'profile.html',context)

    def post(self,request):

        pass