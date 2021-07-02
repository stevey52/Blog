from django.contrib import admin
from .models import Post #new importing our database from models

# Register your models here.
admin.site.register(Post) #registering our Post models to admin
