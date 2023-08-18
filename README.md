# FlexForm 

<!-- # [Vue Soft UI Dashboard](http://demos.creative-tim.com/vue-soft-ui-dashboard/?ref=readme-vsud) [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&logo=twitter)](https://twitter.com/intent/tweet?url=https://www.creative-tim.com/product/vue-soft-ui-dashboard&text=Check%20Vue%20Soft%20UI%20Dashboard%20made%20by%20@CreativeTim%20#webdesign%20#dashboard%20#softdesign%20#vue%20https://www.creative-tim.com/product/vue-soft-ui-dashboard)

![version](https://img.shields.io/badge/version-3.0.0-blue.svg) [![GitHub issues open](https://img.shields.io/github/issues/creativetimofficial/vue-soft-ui-dashboard.svg)](https://github.com/creativetimofficial/vue-soft-ui-dashboard/issues?q=is%3Aopen+is%3Aissue) [![GitHub issues closed](https://img.shields.io/github/issues-closed-raw/creativetimofficial/vue-soft-ui-dashboard.svg)](https://github.com/creativetimofficial/vue-soft-ui-dashboard/issues?q=is%3Aissue+is%3Aclosed)

![Image](https://s3.amazonaws.com/creativetim_bucket/products/591/original/vue-soft-ui-dashboard.jpg)
 -->


## Intro
FlexForm is a WebApplication built using VueJs to create dynamic forms according to your needs in no time.    
This Enables you to create large forms without the hustle to make different database tables for each form you make alongwith the difficulty to manage any changes it encounters to a simple precedure to get the desired Form keeping all the information just to you.    

## Vue FrontEnd
The frontend of FlexForm is build using Vue.js to create a single page web application.     
This was acheived by building the frontend on top of a template and additional pages were added according to the design flow.
### Directions to Start

Clone the project into your directory by using command 
``` bash
git clone 
cd Frontend
```

Then run the basic setup below to start the project frontend on the local device


#### Build Setup

``` bash
# install dependencies
npm install

# To change node version using nvm
nvm use 16

# serve with hot reload at localhost:8080
npm run serve

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report



```


## FlexForm API Backend

The backend of FlexForm is build using Django REST framework to create Dynamic tables/models in it using PostgreSQL as default settings.
Other databases can be configured by extra changes to the settings / python code to work properly

### Setup

First clone the project if not done before by using:
``` bash
git clone 
```
Then switch to the backend directory using
``` bash

cd Backend
```

Next step is to install the dependencies using:

```sh
pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies    
In order to run the application successfully, you'll have to change the database settings in `settings.py` according to your database connection for PostgreSQL connection

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<Database name here>'',
        'USER': '<database username here>'',
        'PASSWORD': '<database password here>',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

To create a localhost connection port for the application to listen at    
`http://127.0.0.1:8000/`   
run
```sh
cd flexform
python manage.py runserver
```

To make migrations to database, run:
```sh
python manage.py makemigrations
python manage.py migrate
```



#### Different API URLs 

The user can request different APIs using different URLs ass following:

##### For Swagger Documentation 
```sh
http://localhost:8000/doc
http://localhost:8000/redoc
```
##### Create User Token 
```sh
http://localhost:8000/api-token-auth/
```
##### User Registeration 
```sh
http://localhost:8000/register/
```
##### User Login 
```sh
http://localhost:8000/login/
```
##### Get all Users 
```sh
http://localhost:8000/get-all-users
```
##### Get User 
```sh
http://localhost:8000/get-user
```
##### Create,Read,Update,Delete Form
```sh
http://localhost:8000/form-api
```
##### Get Form
```sh
http://localhost:8000/get-form/<id>
```
##### Publish Form
```sh
http://localhost:8000/publish-form
```
##### Get Form Responses
```sh
http://localhost:8000/get-response/<id>
```
##### Post Form Responses
```sh
http://localhost:8000/post-response/<id>
```
##### Delete Form Responses
```sh
http://localhost:8000/delete-response
```
##### Approve Form Responses
```sh
http://localhost:8000/approve-response
```



