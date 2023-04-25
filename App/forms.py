from django import forms

#def check_for_a(value):
    #if value[0].lower()=='a':
        #raise forms.ValidationError('Name Started With a')
    
def check_for_a(value):
    if value[0].lower()!='a':
        raise forms.ValidationError('Name Started With a')

#def check_for_len(value):
    #if len(value)<6:
        #raise forms.ValidationError('Length Is Less Than 6 Character')
    
def check_for_len(value):
    if len(value)>6:
        raise forms.ValidationError('Length Is greater Than 6 Character')

class StudentForm(forms.Form):
    #name=forms.CharField(max_length=100,validators=[check_for_a])
    name=forms.CharField(max_length=100,validators=[check_for_a,check_for_len])
    age=forms.IntegerField()
    email=forms.EmailField()