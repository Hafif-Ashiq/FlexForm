from django.urls import path
from .views import *


urlpatterns = [
    path('get-all-users',get_all_users),
    path('register/',RegisterUser.as_view()),
    path('login/',LoginUser.as_view()),
    path('get-user',GetUser.as_view()),
    path('form-api',FormAPI.as_view()),
    path('get-form/<id>', get_form),
    path('publish-form',publishForm),
    path('get-response/<id>',get_responses),
    path('post-response/<id>',post_response),
    path('delete-response',delete_response),
    path('approve-response',approve_response)
]
