from rest_framework import serializers
from .models import *
import re 
from django.apps import apps


from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):



    class Meta:
        model= User
        fields = ['email','password','first_name','last_name','is_staff']
        

    def create(self,validated_data):
        user = User.objects.create(
            username= validated_data['email'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name=validated_data['last_name']
            )
        user.set_password(validated_data['password'])
        user.save()
        return user


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        # fields= "__all__"
        exclude = ['created_at','updated_at']



def makeResponseSerializer(id):
    
    attrs = {
            '__module__': __name__,
            
        }

    class Meta:
        model = apps.get_model(app_label='flexApp', model_name='form_'+ id)
        fields= "__all__"
        # exclude = ['created_at','updated_at']
    attrs['Meta'] = Meta

    serializer = type('Serializer_Form', (serializers.ModelSerializer,), attrs)
    # admin.site.register(model)
    return serializer