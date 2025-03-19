from django.db.models.signals import pre_init, pre_save, pre_migrate, pre_delete, post_init, post_save, post_migrate, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

# def login_success(sender,request,user, **kwargs):
    
