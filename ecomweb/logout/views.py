from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control


@cache_control(no_cache=True, must_revalidate=True)
def logout(request):
    customerID = request.session.get('customer')
    if customerID:  # if user want to access login page after login redirec home page
        request.session.clear()
        return redirect('login')
    else:
        return redirect('/')
