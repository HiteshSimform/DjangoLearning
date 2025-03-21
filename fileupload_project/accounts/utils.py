from django.core.exceptions import PermissionDenied

def role_required(role):
    def decorator(func):
        def wrapper(request,*args,**kwargs):
            if request.user.role==role or request.user.is_superuser:
                return func(request,*args,**kwargs)
            else:
                raise PermissionDenied
        return wrapper
    return decorator