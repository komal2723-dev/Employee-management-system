from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Employee
from django.views import View
from . forms import AddEmployeeForm, FilterEmployeeForm
# Create your views here.

class main_page(View):
    template_name = 'ems/index.html'
    def get(self, request):
        return render(request,self.template_name)
        
class show_all_emp(View):
    template_name =  'ems/show_all_user.html'
    def get(self,request):
        obj = Employee.objects.all()
        return render(request, self.template_name,{"emp":obj})

class add_emp(View):
    template_name = 'ems/add_emp.html'
    def post(self, request):
        obj = AddEmployeeForm(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('showdata')
    def get(self, request): 
        obj = AddEmployeeForm()
        return render(request,self.template_name,{"data" : obj})

class delete_emp(View):
    template_name = 'ems/deletenupdate.html'
    def get(self, request,eid = None):
        if eid == None:
            obj = Employee.objects.all()
        else:
            user = Employee.objects.filter(pk = eid)
            user.delete()
            obj = Employee.objects.all()
        return render(request,self.template_name,{'emp':obj})

class update_Emp(View):
    template_name = 'ems/update_emp.html'
    def post(self,request,id):
        user = Employee.objects.get(pk = id)
        obj = AddEmployeeForm(request.POST, instance=user)
        if obj.is_valid():
            obj.save()
            return redirect('showdata')
    def get(self, request,id):
        user = Employee.objects.get(pk = id)
        obj = AddEmployeeForm(instance=user)
        return render(request,self.template_name,{'data':obj})
    
class filter_Emp(View):
    template_name = 'ems/filteremp.html'
    def post(self, request):
        form = FilterEmployeeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            first_name = data['first_name']
            last_name = data['last_name']
            department = data['dept']
            role = data['role']
            employees = Employee.objects.all()
            if first_name:
                employees = employees.filter(first_name__icontains = first_name)
            if last_name:
                employees = employees.filter(last_name__icontains = last_name)
            if department:
                employees = employees.filter(dept = department)
            if role:
                employees = employees.filter(role = role)
            return render(request,self.template_name,{"form":form,"employees":employees})
    def get(self,request):
        form = FilterEmployeeForm()
        return render(request,self.template_name,{"form":form})