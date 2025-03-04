"""
URL configuration for learningpractice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app1 import views
from app1.views import learn_django

urlpatterns = [
    # path('', include('app1.urls')),
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('myfun/', views.myfunction , name='myfunction'),
    # path('dj/',views.learn_django,name='learn_django'),
    path('dj/',views.learn_django,{'status':'OK'}),
    path('py/',views.learn_python,name='learn_python'),
    path('math/',views.learn_math,name='learn_math'),
    path('php/',views.learn_php,name='learn_php'),
    path('myapp1/',views.myapp1,name='myapp1'),
]
