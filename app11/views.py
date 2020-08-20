from django.shortcuts import render
from django.http import HttpResponse
from app11 import forms
from django.core.files.storage import FileSystemStorage
from app11.utilities import store_img

# Create your views here.

def builtins(request):
    if request.method=="POST":
        form=forms.Form(request.POST,request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            email=form.cleaned_data.get('email')
            phno=form.cleaned_data.get('phno')
            pwd=form.cleaned_data.get('pwd')
            birth_day=form.cleaned_data.get('birth_day')
            birth_month=form.cleaned_data.get('birth_month')
            birth_year=form.cleaned_data.get('birth_year')
            gender=form.cleaned_data.get('gender')
            prog_languages=form.cleaned_data.get('prog_languages')
            languages=form.cleaned_data.get('languages')
            image=form.cleaned_data.get('image')
            store_image(image)
            data=form.cleaned_data
            return render(request,"display_data.html",context=data)
    form=forms.Form()
    return render(request,"builtins.html",{'form':form})