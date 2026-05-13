from django.shortcuts import render
from django.views import *
# Create your views here.

class LoginView(View):
    def get(self,request):
        return render(request, "login.html")

class ProfileView(View):
    def get(self,request,name):
        user=request.user
        profile=ProfileView(user=user)
        social = user.socialaccount_set.filter(provider='google').first()

        avatar = None
        if social:
            avatar = social.get_avatar_url()


        context={
            'name':user,
            'profile':profile,
            'avatar':avatar,
        }

        return render(request,'profile.html',context)

    def post(self,request):

        pass