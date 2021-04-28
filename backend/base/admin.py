from django.contrib import admin
from .models import Person, City, Address, Post

admin.site.register(Person)
admin.site.register(City)
admin.site.register(Address)
admin.site.register(Post)


# Register your models here.
