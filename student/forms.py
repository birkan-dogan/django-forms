from django import forms

# we have two ways to create forms

# first way

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length=30)
    number = forms.IntegerField(required=False)
    profile_image=forms.ImageField(required=False)