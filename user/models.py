# from django.db import models
# from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

#     pronouns = models.CharField(max_length=4, blank=True)

#     short_bio = models.CharField(max_length=160, blank=True)

#     show_claps = models.BooleanField(default=True)
#     show_responses = models.BooleanField(default=True)
#     show_highlights = models.BooleanField(default=True)

#     def __str__(self):
#         return self.user.username