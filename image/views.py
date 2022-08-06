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


# Starting page controller with the list of all loaded images
def index(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'image/index.html', context)


# controller for changing image size page
def one_image(request, image_id):
    image = Image.objects.get(id=image_id)
    proportion = image.width / image.height
    if request.method != 'POST':
        form = ChangeForm()
    else:
        form = ChangeForm(request.POST)
        if form.is_valid():
            # get width and height from form
            width = form['width'].value()
            height = form['height'].value()
            # save proportions
            try:
                width, height = map(int, [width, height])
            except ValueError:
                if height:
                    width = proportion * int(height)
                    width, height = map(int, [width, height])
                elif width:
                    height = int(width) / proportion
                    width, height = map(int, [width, height])

            # construct name of changed image
            name = str(width) + str(height) + str(image)

            # change image size by class Image(as Pillow) from PIL
            im = Pillow.open('{}'.format(MEDIA_ROOT+'/'+str(image.file)))
            out = im.resize((width, height))
            buffer = BytesIO()
            out.save(fp=buffer, format='JPEG')
            buffer.seek(0)
            new_pic = InMemoryUploadedFile(buffer, 'ImageField',
                                           name, 'image/jpeg',
                                           sys.getsizeof(buffer), None)

            # save changed image
            image = ChangedImage.objects.create(file=new_pic)
    context = {'image': image, 'form': form}
    return render(request, 'image/image.html', context)


# controller for adding new image
def new_image(request):
    if request.method != 'POST':
        form = AddForm()
    else:
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():

            # check which form was filled, url or file
            img_url = form.cleaned_data.get('url')
            img_file = form.cleaned_data.get('file')

            if img_file:
                image = form.save()
                image_id = image.id
                return HttpResponseRedirect('../id/{}'.format(image_id))

            elif img_url:
                name = img_url.split('/')[-1]
                image_content = ContentFile(requests.get(img_url).content)
                new_pic = InMemoryUploadedFile(image_content, 'ImageField',
                                               name, 'image/jpeg',
                                               sys.getsizeof(image_content), None)
                image = Image.objects.create(file=new_pic)
                image_id = image.id
                return HttpResponseRedirect('../id/{}'.format(image_id))
    context = {'form': form}
    return render(request, 'image/new_image.html', context)


