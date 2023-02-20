from django.shortcuts import render,HttpResponse
from emp_app.models import Department, Role, Employee
from django.db.models import Q

# Create your views here.
def index(request):
    # return HttpResponse("Hello")
    return render(request, 'index.html')

def all_emp(request):
    emps=Employee.objects.all
    context={
        'emps':emps
    }
    return render(request, 'all_emp.html', context)

def add_emp(request):
    if request.method=="POST":
        first_name=request.POST.get('f_name')
        last_name=request.POST.get('l_name')
        dept=(request.POST.get('dept'))
        salary=request.POST.get('salary')
        bonus=request.POST.get('bonus')
        role=request.POST.get('role')
        phone=request.POST.get('phone')
        hiredate=request.POST.get('hiredate')
    
        new_emp=Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,role_id=role,phone=phone,hiredate=hiredate)
        new_emp.save()
        return HttpResponse("Added successfully")
    elif(request.method=="GET"):
            return render(request, 'add_emp.html')
    else:
        return HttpResponse("Error")

def rem_empl(request):
    emps=Employee.objects.all
    context={
        'emps':emps
    }
    return render(request, 'rem_emp.html',context)

def rem_emp(request, emp_id ):
    if emp_id:
         try:
              emp_rem=Employee.objects.filter(id=emp_id)
              emp_rem.delete()
              return HttpResponse("Employee removed successfully!")
         except:
              return HttpResponse("The id is wrong !")
    emps=Employee.objects.all
    context={
        'emps':emps
    }
    return render(request, 'rem_emp.html', context)
    
def filt_emp(request):
    if(request.method=="POST"):
         name=request.POST.get('flname')
         dept=request.POST.get('dept')
         role=request.POST.get('role')
         emps=Employee.objects.all()
         if name:
              emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
         if dept:
              emps = emps.filter(dept__name= dept)
         if role:
              emps = emps.filter(role__name=role)

         context={
                   'emps':emps
              }
         return render(request, 'all_emp.html', context)

    elif request.method=="GET":
        return render(request,'filt_emp.html')
    else:
         return HttpResponse("Error")
