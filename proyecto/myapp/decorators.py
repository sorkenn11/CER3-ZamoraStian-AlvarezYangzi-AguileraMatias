# decorators.py
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test

def group_required(group_name):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return _wrapped_view
    return decorator


def group_required(group_name):
    def in_groups(user):
        if user.is_authenticated:
            if user.groups.filter(name=group_name).exists() or user.is_superuser:
                return True
        raise PermissionDenied
    return user_passes_test(in_groups)