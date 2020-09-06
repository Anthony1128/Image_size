from django.shortcuts import render
from .models import Image
import os


def index(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'image/index.html', context)


def one_image(request, image_id):
    image = Image.objects.get(id=image_id)
    context = {'image': image}
    return render(request, 'image/image.html', context)
