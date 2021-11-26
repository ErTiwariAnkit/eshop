from django.shortcuts import render, redirect
from django.views import View

from home.models.otp import Otp


class Password_reset(View):
    def get(self, request):
        return render(request, 'core/password_reset_done.html')

    def post(self, request):
        postData = request.POST
        otp=postData.get('otp')
        otp_get = Otp.get_otp()
        print(type(otp))
        print(type(otp_get))
        if int(otp)==otp_get:
            return redirect('password_reset_confirm')
        else:
            return render(request, 'core/password_reset_done.html', {'error': 'Otp is wrong enter correct Otp'})
