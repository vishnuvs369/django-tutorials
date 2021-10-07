# django-tutorials

https://docs.djangoproject.com/en/3.2/intro/tutorial01/

python -m django --version

django-admin startproject demo  --creating a django project

django-admin startproject demo .    --> 

python manage.py runserver -- for running

python manage.py runserver 9000 --specific port

py manage.py startapp products --create an app

pip install mysqlclient

Database  Migrations--->

py manage.py migrate   


Add your app name in INSTALLED_APPS of settings.py

py manage.py makemigrations <appname>

Now, migrate to reflect the changes into the database.
py manage.py migrate  

