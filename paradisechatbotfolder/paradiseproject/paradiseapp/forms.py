from .models import Chatbot
from django import forms
class ChatbotForm(forms.ModelForm):

    class Meta:
        model=Chatbot
        fields=['name','desc','year','img']