from django import forms
from .models import Student
# we have two ways to create forms

# first way
"""
class StudentForm(forms.Form):
    first_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length=30)
    number = forms.IntegerField(required=False)
    profile_image=forms.ImageField(required=False)
"""

# second way

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name","last_name","number","profile_pic"]  # "__all__"
        labels = {"first_name":"Name"}