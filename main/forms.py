from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile,Test
from django.forms import ModelForm


# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(
#         required=True,
#         widget=forms.EmailInput(attrs={
#             'class': 'w-full border-b border-gray-300 focus:border-black outline-none py-3 text-lg bg-transparent',
#             'placeholder': 'Your email',
#         })
#     )
#     first_name = forms.CharField(
#         required=True,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full border-b border-gray-300 focus:border-black outline-none py-3 text-lg bg-transparent',
#             'placeholder': 'Your name',
#         })
#     )

#     class Meta:
#         model = User
#         fields = ('first_name', 'email', 'username', 'password1', 'password2')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name in ['username', 'password1', 'password2']:
#             self.fields[field_name].widget.attrs.update({
#                 'class': 'w-full border-b border-gray-300 focus:border-black outline-none py-3 text-lg bg-transparent',
#             })
#         self.fields['username'].widget.attrs['placeholder'] = 'Username'
#         self.fields['password1'].widget.attrs['placeholder'] = 'Password'
#         self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'


# class SignInForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update({
#             'class': 'w-full border-b border-gray-300 focus:border-black outline-none py-3 text-lg bg-transparent',
#             'placeholder': 'Username or email',
#         })
#         self.fields['password'].widget.attrs.update({
#             'class': 'w-full border-b border-gray-300 focus:border-black outline-none py-3 text-lg bg-transparent',
#             'placeholder': 'Password',
#         })


# class ArticleForm(forms.ModelForm):
#     tags_input = forms.CharField(
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full outline-none text-sm text-gray-500',
#             'placeholder': 'Add up to 5 tags...',
#             'id': 'tags-input',
#         })
#     )

#     class Meta:
#         model = Article
#         fields = ['title', 'subtitle', 'content', 'cover_image', 'status']
#         widgets = {
#             'title': forms.TextInput(attrs={
#                 'class': 'w-full text-4xl font-bold outline-none placeholder-gray-300 border-none',
#                 'placeholder': 'Title',
#             }),
#             'subtitle': forms.TextInput(attrs={
#                 'class': 'w-full text-2xl outline-none placeholder-gray-300 text-gray-600 border-none',
#                 'placeholder': 'Tell your story...',
#             }),
#             'content': forms.Textarea(attrs={
#                 'class': 'w-full min-h-96 outline-none text-lg leading-relaxed border-none resize-none',
#                 'placeholder': 'Write your story...',
#                 'rows': 20,
#                 'id': 'article-content',
#             }),
#             'cover_image': forms.FileInput(attrs={
#                 'class': 'hidden',
#                 'id': 'cover-image-input',
#             }),
#             'status': forms.HiddenInput(),
#         }


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['content']
#         widgets = {
#             'content': forms.Textarea(attrs={
#                 'class': 'w-full border border-gray-200 rounded-lg p-4 outline-none focus:border-gray-400 resize-none text-sm',
#                 'placeholder': 'Write a response...',
#                 'rows': 3,
#             })
#         }


# class ProfileForm(forms.ModelForm):
#     first_name = forms.CharField(
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full border-b border-gray-300 focus:border-black outline-none py-2 bg-transparent',
#         })
#     )
#     last_name = forms.CharField(
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full border-b border-gray-300 focus:border-black outline-none py-2 bg-transparent',
#         })
#     )

#     class Meta:
#         model = Profile
#         fields = ['bio', 'avatar']
#         widgets = {
#             'bio': forms.Textarea(attrs={
#                 'class': 'w-full border-b border-gray-300 focus:border-black outline-none py-2 bg-transparent resize-none',
#                 'rows': 3,
#                 'placeholder': 'Tell the world about yourself',
#             }),
#             'avatar': forms.FileInput(attrs={
#                 'class': 'hidden',
#                 'id': 'avatar-input',
#             }),
#         }




class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'