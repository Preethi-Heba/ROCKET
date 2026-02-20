from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    roll_number = forms.IntegerField()
    email = forms.EmailField()