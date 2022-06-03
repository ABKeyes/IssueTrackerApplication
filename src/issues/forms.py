from django import forms

from issues.models import Issue, IssueComment

status_choices = (
    ("Open", "Open"),
    ("Closed", "Closed"),
    ("Discontinued", "Discontinued"),
)

class CreateIssueForm(forms.ModelForm):
    issueName = forms.CharField(required=True,
                                max_length=50,
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "Issue Name",
                                        }))
    description = forms.CharField(required=True,
                                  max_length=200,
                                  widget=forms.Textarea(
                                      attrs={
                                          "placeholder": "Description",
                                          }))

    status = forms.ChoiceField(choices = status_choices)

    class Meta:
        model = Issue
        fields = ['issueName', 'description', 'status']

class UpdateIssueForm(forms.ModelForm):
    description = forms.CharField(required=True,
                                  max_length=200,
                                  widget=forms.Textarea(
                                      attrs={
                                          "placeholder": "Description",
                                          }))

    status = forms.ChoiceField(choices = status_choices)

    class Meta:
        model = Issue
        fields = ['description', 'status']

class issueComment(forms.ModelForm):
    description = forms.CharField(required=True,
                                  max_length=200,
                                  widget=forms.TextInput(
                                      attrs={
                                          "placeholder": "Insert new comment.",
                                          }))
    class Meta:
        model = IssueComment
        fields = ['description']