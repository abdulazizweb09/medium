from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import TestForm
# Create your views here.

class HomeView(View):
    def get(self,request):
        if request.user.is_authenticated:
            user=request.user
            post=Test.objects.all().order_by('-created_at')
            social = user.socialaccount_set.filter(provider='google').first()
            avatar=None


            if social and social.get_avatar_url():
                avatar = social.get_avatar_url()

                if Profile.objects.get(user=user):
                    profile = Profile.objects.get(user=user)
                    profile.avatar = avatar
                    profile.save()

            else:
                profile = Profile.objects.get(user=user)
                avatar=profile.avatar    
        
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
    

class DetailsView(View):
    def get(self,request,id):
        post=Test.objects.get(id=id)

        session_key = f'viewed_post_{post.id}'

        if not request.session.get(session_key):
            post.views += 1
            post.save()

            request.session[session_key] = True

        context={
            'post':post,
        }

        return render(request,'details.html',context)
    
    def post(self,request):

        pass