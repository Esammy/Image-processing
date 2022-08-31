from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField( upload_to='images')


    def __str__(self):
        return self.title

class Dwt_img(models.Model):
    name = models.CharField(default='Dwt_img_name',max_length=50)
    image = models.ImageField(upload_to = 'dwt_images')

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url