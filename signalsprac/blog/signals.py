from django.contrib.auth.signals import user_logged_in, user_logged_out,user_login_failed
from django.contrib.auth.models import User

from django.db.models.signals import pre_init,pre_save,pre_migrate,pre_delete,post_init,post_save,post_migrate,post_delete


from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def login_success(sender,request,user,**kwargs):
    print("-------------------")
    print("Logged-in Signal... Run Intro....")
    print("Sender:",sender)
    print("Request:",request)
    print("User:",user)
    print("User Password:",user.password)
    print(f'Kwargs: {kwargs}')

# user_logged_in.connect(login_success,sender=User)


def logout_success(sender,request,user,**kwargs):
    print("-------------------")
    print("Logged-out Signal... Run Outro....")
    print("Sender:",sender)
    print("Request:",request)
    print("User:",user)
    print("User Password:",user.password)
    print(f'Kwargs: {kwargs}')

user_logged_out.connect(logout_success,sender=User)

def login_failed(sender,credentials,request,**kwargs):
    print("-------------------")
    print("Logged-in Failed Signal... ")
    print("Sender:",sender)
    print("Request:",request)
    print("Credentials:",credentials)
    print(f'Kwargs: {kwargs}')

user_login_failed.connect(login_failed)


# Pre-save
@receiver(pre_save,sender=User)
def at_beginning_save(sender,instance,**kwargs):
    print("-------------------")
    print("Pre Save Signal... ")
    print("Sender:",sender)
    print("Instance:",instance)
    print(f'Kwargs: {kwargs}')

# Post-save
@receiver(post_save,sender=User)
def at_endiing_save(sender,instance,created,**kwargs):
    if created:
        print("-------------------")
        print("Post Save Signal... ")
        print("New Record")
        print("Sender:",sender)
        print("Instance:",instance)
        print("Created : ",created)
        print(f'Kwargs: {kwargs}')
    else:
        print("-------------------")
        print("Post Save Signal... ")
        print("Update Record")
        print("Sender:",sender)
        print("Instance:",instance)
        print("Created : ",created)
        print(f'Kwargs: {kwargs}')

@receiver(pre_delete,sender=User)
def at_beginning_delete(sender,instance,**kwargs):
    print("-------------------")
    print("Pre Delete Signal... ")
    print("Sender:",sender)
    print("Instance:",instance)
    print(f'Kwargs: {kwargs}')

@receiver(post_delete,sender=User)
def at_ending_delete(sender,instance,**kwargs):
    print("-------------------")
    print("Post Delete Signal... ")
    print("Sender:",sender)
    print("Instance:",instance)
    print(f'Kwargs: {kwargs}')

@receiver(pre_init,sender=User)
def at_beginning_init(sender,*args,**kwargs):
    print("-------------------")
    print("Pre Init Signal... ")
    print("Sender:",sender)
    print(f'Kwargs: {kwargs}')

@receiver(post_init,sender=User)
def at_ending_init(sender,*args,**kwargs):
    print("-------------------")
    print("Post Init Signal... ")
    print("Sender:",sender)
    print(f'Kwargs: {kwargs}')


# Request / Response Signals
