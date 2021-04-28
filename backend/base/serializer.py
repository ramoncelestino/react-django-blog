from rest_framework import serializers
from .models import Person
from .models import Address
from .models import Post



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Person
        fields = ('id', 'name', 'email', 'phone', 'address') 

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = '__all__'
        


