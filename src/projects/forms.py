from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    user = forms.CharField(required=True, max_length=150, )
    name = forms.CharField(required=True, 
                           max_length=50, 
                           widget=forms.TextInput(
                                      attrs={
                                          "placeholder": "Project Name",
                                          }))
    summary = forms.CharField(required=False, 
                              max_length=200, 
                              widget=forms.Textarea(
                                  attrs={
                                        "placeholder": "Summary"}))
    description = forms.CharField(required=False, 
                                  max_length=2000, 
                                  widget=forms.Textarea(
                                      attrs={
                                          "placeholder": "Description"}))

    class Meta:
        model = Project
        fields = [
            'user',
            'name',
            'summary',
            'description',
            ]