from .models import SnackSQL
from django.contrib import admin
		
admin.site.register(SnackSQL)
#adds names to items in db

def __str__(self):
      return self.name
