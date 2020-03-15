from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageForm


# Create your views here.
def index(request):
    form = ImageForm()
    if request.method == 'POST':
        print("POST received")
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin')

    return render(request, 'ImgHub/index.html', {'form': form})