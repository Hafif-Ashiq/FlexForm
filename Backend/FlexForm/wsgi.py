"""
WSGI config for FlexForm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FlexForm.settings')


# Run the migrations for published forms at start of server once to make models dynamically

from flexApp.serializer import *
from flexApp.models import *
from django.core import management
forms = Form.objects.all()

for form in forms:
    serializer = FormSerializer(form)
    if serializer.data['published']:
        response_form = form.makeResponseModel()
    
management.call_command('makemigrations', 'flexApp')
management.call_command('migrate', 'flexApp')




from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()


