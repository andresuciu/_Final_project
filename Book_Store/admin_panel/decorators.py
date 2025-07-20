from django.http import HttpResponse

def admin_required(view_func):
    def wrapper_view(request, *args, **kwareg):
        if request.user.is_authenticated and request.user.role=='admin':
            return view_func(request, *args, **kwareg)
        else:
            return HttpResponse("Access only to admin users.")

    return wrapper_view

