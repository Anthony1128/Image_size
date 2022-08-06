# Upload and transformation image service

## Description

Service, based on framework [Django](https://www.djangoproject.com/), which allows uploading an image from users local storage, or by link, and then change its size.

The home screen displays a list of downloaded images. Initially it is empty. At the bottom of the list there is a link to add an image.

It is possible to add an image by entering a link or by selecting a file from local storage. Submitting the form is allowed only when one field of the form is filled.

After a successful upload, we get to the image page. Initially, the image is displayed in its original size. Through the form, you can set new dimensions. After submitting the form, the page will refresh and the image will be with the new dimensions.
You can specify just the width, just the height, or both. 
Image proportions are preserved when only one size is submitted.

From the image page and from the page for adding an image, you can go back to the general list of images.

## Deployment and run instruction

To start the app follow next steps:
1. install dependecies `python -m pip install -r requirements.txt`
2. make database migrations `python manage.py makemigrations`
3. apply migrations `python manage.py migrate`
4. run the app `python manage.py runserver`

