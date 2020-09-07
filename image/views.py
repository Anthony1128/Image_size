import sys
from io import BytesIO
from PIL import Image as Pillow
import requests
from django.core.files.base import ContentFile
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.uploadedfile import InMemoryUploadedFile
from image_size.settings import MEDIA_ROOT
from .models import Image, ChangedImage
from .forms import AddForm, ChangeForm


def index(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'image/index.html', context)


def one_image(request, image_id):
    image = Image.objects.get(id=image_id)
    if request.method != 'POST':
        form = ChangeForm()
    else:
        form = ChangeForm(request.POST)
        if form.is_valid():
            width = int(form['width'].value())
            height = int(form['height'].value())
            name = str(width) + str(height) + str(image)
            im = Pillow.open('{}'.format(MEDIA_ROOT+'/'+str(image.file)))
            out = im.resize((width, height))
            buffer = BytesIO()
            out.save(fp=buffer, format='JPEG')
            buffer.seek(0)
            new_pic = InMemoryUploadedFile(buffer, 'ImageField',
                                           name, 'image/jpeg',
                                           sys.getsizeof(buffer), None)
            image = ChangedImage.objects.create(file=new_pic)
    context = {'image': image, 'form': form}
    return render(request, 'image/image.html', context)


def new_image(request):
    if request.method != 'POST':
        form = AddForm()
    else:
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            img_url = form.cleaned_data.get('url')
            img_file = form.cleaned_data.get('file')
            if img_file:
                image = form.save()
                image_id = image.id
                return HttpResponseRedirect('../{}'.format(image_id))
            elif img_url:
                name = img_url.split('/')[-1]
                image_content = ContentFile(requests.get(img_url).content)
                new_pic = InMemoryUploadedFile(image_content, 'ImageField',
                                               name, 'image/jpeg',
                                               sys.getsizeof(image_content), None)
                image = Image.objects.create(file=new_pic)
                image_id = image.id
                return HttpResponseRedirect('../{}'.format(image_id))
    context = {'form': form}
    return render(request, 'image/new_image.html', context)


