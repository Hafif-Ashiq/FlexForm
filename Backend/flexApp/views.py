from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.apps import apps


from django.core import management
from django.contrib.auth import authenticate


# Create your views here.
import re

def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s

def make_migrations():
    # try:
        # Replace 'your_app_name' with the name of your app or leave it as None to make migrations for all apps.
        management.call_command('makemigrations', 'flexApp')
        management.call_command('migrate', 'flexApp')

        print("Migrations have been created successfully.")
    # except Exception as e:
    #     print(f"An error occurred while running migrations: {e}")
     

@api_view(['GET'])
def get_all_users(request):
    try:
        # make_migrations()
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        return Response({
            "status" : 404 
        })



class RegisterUser(APIView):
    def post(self,request):
        try:
            
            serializer = UserSerializer(data = request.data)

            if serializer.is_valid():
                serializer.save()
                user = User.objects.get(email = serializer.data['email'])
                token_obj , _ = Token.objects.get_or_create(user = user)
                return Response({
                    'status' : 200,
                    'data' : serializer.data,
                    'token' : str(token_obj)
                })
            return Response(serializer.errors)
        except Exception as e:
            print(e)
            return Response({
                'status' : "Error"
            })
        
    def patch(self,request):
        try:
            obj = User.objects.get(email=request.data['email'])

            serializer = UserSerializer(obj,data = request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status' : 200,
                    'data' : serializer.data,
                    
                })
            return Response(serializer.errors)
        except Exception as e:
            print(e)
            return Response({
                'status' : "Error"
            })
        

class LoginUser(APIView):
    def post(self,request):
        try:
            
            username=request.data["email"]
            password=request.data["password"]
            user = authenticate(request, username=username, password=password)
            
            
            if(user is not None):
                token_obj , _ = Token.objects.get_or_create(user = user)
                return Response({
                'status' : True,
                'token' : str(token_obj)
                
            })
            return Response({
                'status' : False
            })
        except Exception as e:
            print(e)
            return Response({
                'status' : False
            })
        

        
class GetUser(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            # print(request.data)
            user_id = Token.objects.get(key=request.data['token']).user_id
            user = User.objects.get(id=user_id)

            return Response({
                'status' : True,
                "email": user.email,
                "first_name" : user.first_name,
                "last_name" : user.last_name 
            })
        except Exception as e:
            print(e)
            return Response({
                'status' : False,
                # "username": user.username 
            })


class FormAPI(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def post(self,request):
        # try:
            token = request.META.get('HTTP_AUTHORIZATION')
            token = token.split(' ')
            token = token[1]
            print(token)
            
            user_id = Token.objects.get(key=token).user_id
            data = request.data
            data['user_id'] = user_id
            data['slug'] = slugify(data['title'])
            # print(data)
            serializer = FormSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                # print(responseform)
                return Response({
                    "status" : True,
                    'data' : serializer.data
                })
            return Response(serializer.errors)
        # except Exception as e:
        #     print(e)
        #     return Response({
        #         'status' : 404
        #     })

    def get(self,request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION')
            token = token.split(' ')
            token = token[1]
            
            user_id = Token.objects.get(key=token).user_id
            forms = Form.objects.filter(user_id = user_id)

            serializer = FormSerializer(forms,many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'status' : 404
            })

    def delete(self,request):
        
        forms = Form.objects.filter(id = request.data['id'])
        print(forms)
        forms.delete()
         
        return Response({
        'status' : True
        })
            
    def patch(self,request):
        data = request.data

        form = Form.objects.get(id = data['id'])

        serializer = FormSerializer(form,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            
            
            return Response(serializer.data)
            
        return Response(serializer.errors)


@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def publishForm(request):
    data = request.data

    form = Form.objects.get(id = data['id'])
    
    
    serializer = FormSerializer(form,data=data,partial=True)
    if serializer.is_valid():
        serializer.save()
        responseform = form.makeResponseModel()
        
        make_migrations()
        data['form_table'] = 'flexApp_form_'+data['id']
        data['published'] = True
        serializer = FormSerializer(form,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
        
            return Response(serializer.data)
        return Response(serializer.errors)
    return Response(serializer.errors)
    


@api_view(['GET'])

def get_form(request,id):
    try:
        # make_migrations()
        form = Form.objects.get(id=id)
        
        fields = ''
        serializer = FormSerializer(form)
        
        if serializer.data['published']:
            response_table = apps.get_model(app_label='flexApp', model_name='form_'+ str(id))
            
            fields = [field.name for field in response_table._meta.get_fields()]
        return Response({
            'data' : serializer.data,
            'fields' : fields
        })
    except Exception as e:
        print(e)
        return Response({
            "status" : 404 
        })
    
@api_view(['POST'])

def post_response(request,id):
    serializerClass = makeResponseSerializer(id)
    data = request.data
    serializer = serializerClass(data=data)

    # print(data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

def get_responses(request,id):
    response_table = apps.get_model(app_label='flexApp', model_name='form_'+ str(id))
    serializerClass = makeResponseSerializer(id)
    responses = response_table.objects.all()
    serializer = serializerClass(responses,many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def approve_response(request):
    print(request.data)
    response_table = apps.get_model(app_label='flexApp', model_name='form_'+ str(request.data['form_id']))
    serializerClass = makeResponseSerializer(request.data['form_id'])
    response = response_table.objects.get(id = request.data['id'])
    serializer = serializerClass(response,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return  Response(serializer.errors)
            

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

def delete_response(request):
    print(request.data)
    response_table = apps.get_model(app_label='flexApp', model_name='form_'+ request.data['form_id'])
    responses = response_table.objects.filter(id = request.data['response_id'])
    print(responses)
    enteries = responses.delete()
    return Response({
        'status'  :"Enteries Deleted: " + str(enteries) 
    })