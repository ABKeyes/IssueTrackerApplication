from django import forms
from .models import Project

status_choices = (
    ("Open", "Open"),
    ("Closed", "Closed"),
    ("Discontinued", "Discontinued"),
)

class ProjectForm(forms.ModelForm):
    #user = forms.CharField(max_length=150)
    name = forms.CharField(required=True, 
                           max_length=50, 
                           widget=forms.TextInput(
                                      attrs={
                                          "placeholder": "Project Name",
                                          }))
    summary = forms.CharField(required=True, 
                              max_length=200, 
                              widget=forms.Textarea(
                                  attrs={
                                        "placeholder": "Summary"}))
    description = forms.CharField(required=False, 
                                  max_length=2000, 
                                  widget=forms.Textarea(
                                      attrs={
                                          "placeholder": "Description"}))
    status = forms.ChoiceField(choices = status_choices)

    class Meta:
        model = Project
        fields = ['name', 'summary', 'description', 'status']