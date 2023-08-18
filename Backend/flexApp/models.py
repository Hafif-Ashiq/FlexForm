import json
import uuid
from django import utils
from django.db import models
from django.core.cache import cache
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.contrib import admin

# from django.contrib.auth.models import AbstractUser

# Create your models here.

User._meta.get_field('email').blank = False
User._meta.get_field('first_name').blank = False
User._meta.get_field('last_name').blank = False
User._meta.get_field('email')._unique = True
User._meta.get_field('is_staff').editable = False


class BaseModel(models.Model):
    # uid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)


    class Meta:
        abstract = True


class Form(BaseModel):
    title = models.CharField()
    description = models.CharField(default="",blank=True)
    meta = models.TextField(default="")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # slug = models.UUIDField(editable=False,default=uuid.uuid4)
    published = models.BooleanField(default=False)
    form_table = models.CharField(default="",blank=True)

    @property
    def makeResponseModel(self):
        
        attrs = {
            '__module__': __name__,
            
        }

        class Meta:
            app_label = 'flexApp'
            verbose_name = self.title + ' Response'
            # managed = False
        attrs['Meta'] = Meta

        
        
        if self.meta != '':
            attrs['created_at'] = models.DateTimeField(auto_now_add=True)
            attrs['approved'] = models.BooleanField(default=False)

            sections = json.loads(self.meta)['sections']
            index = 0
            for section in sections:
                for question in section['questions']:
                    field_name = question['question'].replace(' ','_')
                    
                    if question['type'] == 'textarea':
                        attrs[field_name +  str(index)] = models.TextField(default="")
                    elif question['type'] == 'date':
                        attrs[field_name + str(index)] = models.DateField()
                    elif question['type'] == 'file':
                        attrs[field_name + str(index)] = models.FileField(upload_to ='uploads/', null=True)
                    elif question['type'] == 'checkbox' or  question['type'] == 'multiplechoice':
                        attrs[field_name +  str(index)] =models.CharField()
                    else:
                        attrs[field_name +  str(index)] = models.CharField(default="")
                    
                    index += 1


        model = type('Form_'+str(self.id), (models.Model,), attrs)
        admin.site.register(model)

        return model




