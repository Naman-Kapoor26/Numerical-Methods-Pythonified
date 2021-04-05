from django.shortcuts import render, HttpResponse
from sympy import Derivative,symbols
from math import sin,cos,log,pi
# Create your views here.
def index(request):
    #return HttpResponse('Happy holi')
    #context = {
   #     'variable':"Just kidding"
   # }
    return render(request,'index.html')
def about(request):
    #HttpResponse('By N')
    return render(request,'about.html')
def services(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def N_R_input(request):
    return render(request,'N_R_input.html')
def Secant_input(request):
    return render(request,'Secant_input.html')
def Secant_output(request):
    exp=request.POST.get('expression')
    a=request.POST.get('a')
    a=int(a)
    b=request.POST.get('b')
    b=int(b)
    num_decimal=request.POST.get('num_dec')
    num_decimal=int(num_decimal)
    def funct(fun,h,correct):
        fun_=fun.replace('x',h)
        round(eval(fun_),correct)
        return round(eval(fun_),correct)
    def secant(fun,a,b,correct):
        d={}
        d['x'+str(0)]=a
        d['x'+str(1)]=b
        for i in range(1,6):
            d['x'+str(i+1)]=round(float(d['x'+str(i-1)])-((float(d['x'+str(i)])-float(d['x'+str(i-1)]))*funct(fun,str(d['x'+str(i-1)]),correct+2)/(funct(fun,str(d['x'+str(i)]),correct+2)-funct(fun,str(d['x'+str(i-1)]),correct+2))),correct+2)
            if d['x'+str(i+1)]==d['x'+str(i)]:
                break
            for j in range(i+2,6):
                d['x'+str(j)]=d['x'+str(i+1)]
            
        return d
    Dict=secant(exp,a,b,num_decimal)
    context={   'num1':Dict['x1'],
                'num2':Dict['x2'],
                'num3':Dict['x3'],
                'num4':Dict['x4'],
                'num5':Dict['x5']


        }
    return render(request,'result_secant.html',context)

def N_R_output(request):
    exp=request.POST.get('expression')
    a=request.POST.get('a')
    a=int(a)
    b=request.POST.get('b')
    b=int(b)
    num_decimal=request.POST.get('num_dec')
    num_decimal=int(num_decimal)
    def funct(fun,h,correct):
        fun_=fun.replace('x',h)
        round(eval(fun_),correct)
        return round(eval(fun_),correct)
    
    x=symbols('x')
       
    def N_R(fun,a,b,correct):
        d={}
        d['x'+str(0)]=(a+b)/2
        for i in range(1,6):
            d['x'+str(i)]=round(d['x'+str(i-1)]-round(funct(fun,str(d['x'+str(i-1)]),correct+2)/funct(str(Derivative(fun,x).doit()),str(d['x'+str(i-1)]),correct+2),correct+2),correct+2)
        return d
    Dict=N_R(exp,a,b,num_decimal)
    context={   'num1':Dict['x1'],
                'num2':Dict['x2'],
                'num3':Dict['x3'],
                'num4':Dict['x4'],
                'num5':Dict['x5']


        }
    return render(request,'result_NR.html',context)

#def 