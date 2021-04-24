from django.contrib import admin
from .models import Person
from .models import City 
from .models import Address

admin.site.register(Person)
admin.site.register(City)
admin.site.register(Address)


# Register your models here.
