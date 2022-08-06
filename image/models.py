import os
from django.db import models


# loading image model
class Image(models.Model):
    file = models.ImageField(upload_to='origin/', blank=True,
                             height_field="height", width_field="width",)
    width = models.PositiveIntegerField(default=file.width_field, null=True, blank=True)
    height = models.PositiveIntegerField(default=file.height_field, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        filename = os.path.basename(self.file.name)
        return filename


# changed image model
class ChangedImage(models.Model):
    file = models.ImageField(upload_to='changed')

    def __str__(self):
        filename = os.path.basename(self.file.name)
        return filename

