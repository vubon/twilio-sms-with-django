from django.shortcuts import render, redirect
from twilio.rest import Client
from django.conf import settings

from django.contrib import messages

# Create your views here.
from django.views.generic.base import View


class SendMessageView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        full_mobile = '+88'+mobile

        client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
        try:
            message = client.messages.create(
                to=full_mobile,
                from_=settings.FROM_NUMBER,
                body=message
            )
            if message.sid:
                messages.success(request, 'Successfully sent your message.')
                return redirect('/')
            else:
                messages.info(request, 'Sorry there is a problem.')

        except Exception as e:
            messages.error(request, 'Sorry there is a problem.')
            return redirect('/')
