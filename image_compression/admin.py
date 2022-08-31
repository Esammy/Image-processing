from django.contrib import admin
from .models import Image, Dwt_img

# Registering my models
admin.site.register(Image)
admin.site.register(Dwt_img)