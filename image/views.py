from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Image
from .forms import AddForm


def index(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'image/index.html', context)


def one_image(request, image_id):
    image = Image.objects.get(id=image_id)
    context = {'image': image}
    return render(request, 'image/image.html', context)


def new_image(request):
    if request.method != 'POST':
        form = AddForm()
    else:
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../')
    context = {'form': form}
    return render(request, 'image/new_image.html', context)


