import os
from django.db import models


class Image(models.Model):
    file = models.ImageField(upload_to='origin/', blank=True)
    width = models.PositiveIntegerField(default=file.width_field, null=True, blank=True)
    height = models.PositiveIntegerField(default=file.height_field, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        filename = os.path.basename(self.file.name)
        return filename

class ChangedImage(models.Model):
    file = models.ImageField(upload_to='changed')

    def __str__(self):
        filename = os.path.basename(self.file.name)
        return filename

