from django import forms
from django.core import validators
from . models import Employee, Department, Role
from django.core.exceptions import ValidationError

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'dept', 'salary', 'bonus', 'role', 'number', 'hire_date']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'dept':'Department',
            'salary': 'Salary',
            'bonus': 'Bonus',
            'role': 'Role',
            'number': 'Phone Number',
            'hire_date': 'Joining Date'
        }

        widgets = {
            'first_name':forms.TextInput(attrs={'type':'text','class':"form-control", 'id':"exampleInputFirstName1" ,'placeholder':'Enter your first name'}),
            'last_name':forms.TextInput(attrs={'type':'text','class':"form-control", 'id':"exampleInputLastName1" ,'placeholder':'Enter your last name'}),
            'dept': forms.Select(attrs={'class':'form-control','id':'exampleInputDepartment'}),
            'salary':forms.TextInput(attrs={'type':'number','class':"form-control", 'id':"exampleInputSalary"}),
            'bonus':forms.TextInput(attrs={'type':'number','class':"form-control", 'id':"exampleInputBonus"}),
            'role': forms.Select(attrs={'class':'form-control','id':'exampleInputRole1'}),
            'number':forms.TextInput(attrs={'type':'text','class':"form-control", 'id':"exampleInputBonus"}),
            'hire_date':forms.DateInput(attrs={'type':'date','class':"form-control", 'id':"exampleInputBonus"}, format="%d%m%Y")
        }


class FilterEmployeeForm(forms.Form):
    first_name = forms.CharField(
        required=False,
        label='First Name',
        widget=forms.TextInput(attrs={'type':'text','class':"form-control", 'id':"exampleInputFirstName1" ,'placeholder':'Search by First Name.....'})
    )

    last_name = forms.CharField(
        required=False,
        label='Last Name',
        widget=forms.TextInput(attrs={'type':'text','class':"form-control", 'id':"exampleInputFirstName1" ,'placeholder':'Search by Last Name.....'})
    )

    dept = forms.ModelChoiceField(
        required=False,
        queryset= Department.objects.all(),
        label= 'Department',
        widget= forms.Select(attrs={'class':'form-control','id':'exampleInputDepartment'})    
    )

    role = forms.ModelChoiceField(
        required=False,
        queryset= Role.objects.all(),
        label= 'Role',
        widget= forms.Select(attrs={'class':'form-control','id':'exampleInputDepartment'})    
    )
    