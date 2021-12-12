import subprocess
from django.http import request

from subprocess import SubprocessError, run, PIPE
import requests
#import req
import sys
from django.shortcuts import render

def button(python1):
    return render(python1, 'home.html')

#def output(req):
    
   # data = requests.get("https://www.google.com/")
  #  print(data.text)
  #  data = data.text
   # return render(req, 'home.html', {'data': data})

def external(python1):
    inp= python1.POST.get('param')

    out =run([sys.executable,"C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python39\\django\\python1.py",inp],shell= False,stdout = PIPE)
    print(out)
    return render(python1, 'home.html',{'data1':out.stdout})

def external1(python2):
    inp= python2.POST.get('param1')

    out =run([sys.executable,"C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python39\\django\\python2.py",inp],shell= False,stdout = PIPE)
    print(out)
    return render(python2, 'home.html',{'data2':out.stdout})

def external2(python3):
    inp= python3.POST.get('param2')

    out =run([sys.executable,"C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python39\\django\\python3.py",inp],shell= False,stdout = PIPE)
    print(out)
    return render(python3, 'home.html',{'data3':out.stdout})        