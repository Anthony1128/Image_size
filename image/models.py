from django.db import models
import os


class Image(models.Model):
    file = models.ImageField(upload_to='origin/')
    # width = file.width_field
    # height = file.height_field

    def __str__(self):
        filename = os.path.basename(self.file.name)
        return filename
