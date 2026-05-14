from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, max_length=500)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"{self.user.username}"
 
    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        initials = self.user.username[0].upper()
        return f"https://ui-avatars.com/api/?name={initials}&background=1a8917&color=fff&size=128"
 
    def followers_count(self):
        return self.followers.count()


class Test(models.Model):
    title=models.CharField(max_length=100)
    body=RichTextUploadingField()

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    claps = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    is_published = models.BooleanField(default=True)
    allow_comments = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# class Post(models.Model):
#     ch=[
#         ('Python','Python'),
#         ('Java','Java'),
#         ('Javascript','Javascript'),
#         ('C++','C++'),
#         ('PHP','PHP'),
#     ]


#     author = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="posts"
#     )

#     title = models.CharField(max_length=250)
#     subtitle = models.CharField(max_length=300, blank=True)
#     content = models.TextField()

#     cover_image = models.ImageField(
#         upload_to='posts/',
#         blank=True,
#         null=True
#     )

#     slug = models.SlugField(unique=True)
#     tags = models.CharField(max_length=200, blank=True) 

#     leng=models.CharField(choices=ch, max_length=10,blank=True,null=True)



#     claps = models.PositiveIntegerField(default=0)
#     views = models.PositiveIntegerField(default=0)

#     is_published = models.BooleanField(default=True)
#     allow_comments = models.BooleanField(default=True)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
    


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username