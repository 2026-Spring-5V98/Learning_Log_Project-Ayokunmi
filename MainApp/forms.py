from django import forms

from .models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic 
        fields = ['text'] #'_all_', brings in all the fields
        labels = {'text':''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry 
        fields = ['text'] #'_all_', brings in all the fields
        labels = {'text':''}

        widgets = {'text':forms.Textarea(attrs = {'cols':80})}