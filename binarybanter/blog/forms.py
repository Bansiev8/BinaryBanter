from django import forms
from .models import Post, Subscription, QuesModel


class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets:{
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'post_tags': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
    

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']

class addQuestionform(forms.ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"