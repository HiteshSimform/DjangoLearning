# DjangoLearning

# Django Learning README

## Introduction
Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. This guide will help you revise key concepts and provide structured learning steps.

---

## 1. Setting Up Django
### 1.1 Install Virtual Environment
```sh
pip install virtualenv
```

### 1.2 Create a Virtual Environment
```sh
virtualenv venv  # Create virtual environment
source venv/bin/activate  # Activate (Mac/Linux)
venv\Scripts\activate  # Activate (Windows)
```

### 1.3 Install Django
```sh
pip install django
```

---

## 2. Creating a Django Project
### 2.1 Create a Django Project
```sh
django-admin startproject project_name
```
This creates the following structure:
```
project_name/
│-- manage.py  # Django command-line tool
│-- project_name/  # Project settings and configuration
    │-- __init__.py
    │-- settings.py  # Main settings file
    │-- urls.py  # URL configurations
    │-- asgi.py  # ASGI entry point
    │-- wsgi.py  # WSGI entry point
```

### 2.2 Running the Django Server
```sh
python manage.py runserver  # Runs on default 127.0.0.1:8000
python manage.py runserver 8080  # Runs on a specific port
```

---

## 3. Creating a Django Application
### 3.1 Create an App
```sh
python manage.py startapp app_name
```

### 3.2 Application Folder Structure
```
app_name/
│-- migrations/  # Database migrations
│-- __init__.py
│-- admin.py  # Admin panel configurations
│-- apps.py  # App configuration
│-- models.py  # Database models
│-- tests.py  # Unit tests
│-- views.py  # Handles requests and responses
```

### 3.3 Registering the App in `settings.py`
Add the app to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_name',
]
```

---

## 4. URLs and Views
### 4.1 Defining URLs
Create `urls.py` in the app directory:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

Include the app URLs in the project’s `urls.py`:
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_name.urls')),
]
```

### 4.2 Function-Based Views
Modify `views.py`:
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Home Page")

def about(request):
    return HttpResponse("About Page")
```

Run the server and visit `http://127.0.0.1:8000/about/` to see the output.

---

## 5. Creating Multiple Applications
Django allows multiple applications within a project. Each app handles a specific function of the website.
```sh
python manage.py startapp blog
python manage.py startapp shop
```
- `blog/` → Handles blog-related views
- `shop/` → Handles eCommerce-related views

Include their URLs in `project/urls.py`:
```python
urlpatterns = [
    path('blog/', include('blog.urls')),
    path('shop/', include('shop.urls')),
]
```

---

## Summary
- Set up Django using Virtualenv
- Created a Django project and understood its structure
- Ran Django on different ports
- Created Django applications
- Worked with function-based views
- Managed multiple apps and URL configurations

This serves as a strong foundation for your Django learning journey!


#### Dt : 05-03-2025
- Django URL Patterns
- Django Templates
- Django Template Language

#### Dt : 06-03-2025
- Django Template Inheritance Started