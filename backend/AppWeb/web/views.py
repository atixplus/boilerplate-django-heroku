from django.shortcuts import render, redirect
from django.urls import reverse

from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from .models import State
from django.template.loader import get_template

# import sendgrid
# from sendgrid.helpers.mail import Email, Content, Mail, CustomArg


def home(request):
    return render(request, 'web/login.html', locals())

def enlist_users(request):
    print('here a power line')
    users = User.objects.all()
    for user in users:
        user.states = State.objects.filter(user=user)
    return render(request, 'web/er/users/list.html', locals())

def invite_user(request):
    print('ya tengo el poder!')
    if request.method == 'POST':
        try:
            user = User()
            user.first_name = request.POST.get('name')
            user.username = request.POST.get('email')
            user.email = user.username            
            user.save()
            rol = request.POST.get('rol')
            context = {
                'first_name': user.first_name,
                'rol': rol
            }

            html_content = get_template('web/mailing/base.html').render(context)
            emailMessage = EmailMessage(
                'Hola ' + user.first_name,
                html_content,
                settings.FROM_EMAIL,
                [user.email],
                [],
                reply_to=['another@gmail.com'],
                headers={'Message-ID': 'message-id:'+str(user.id)},
            )
            emailMessage.content_subtype = "html"
            emailMessage.send()
            return redirect(reverse('web:er-users-list'))
        except Exception as e:
            print(str(e))
    return render(request, 'web/er/users/form.html', locals())            

@csrf_exempt
@require_POST
def sendgrid_webhook(request):
    if request.method == 'POST':
        eventsMessage = json.loads(request.body)
        print(eventsMessage)
        try:
            for eventMessage in eventsMessage:
                user = User.objects.get(email=eventMessage['email'])
                message = eventMessage['event']
                timestamp = eventMessage['timestamp']
                State.objects.create(user=user, event=message, timestamp=timestamp)
        except Exception as e:
            print(str(e))

    return HttpResponse()


# def send_email(origin, _from, to, subject, content, attachment=None, cc=None, register_pk=None):
#     """Returns (success, error)"""    

#     try:
#         sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
#         from_email = Email(name=origin, email=_from)
#         to_email = Email(to)
#         content = Content("text/html", content)

#         mail = Mail(from_email, subject, to_email, content)
#         if isinstance(attachment, list):
#             for at in attachment:
#                 mail.add_attachment(at)

#         if register_pk:
#             mail.add_custom_arg(CustomArg("register_pk", str(register_pk)))
      
#         response = sg.client.mail.send.post(request_body=mail.get())
#         if response.status_code == 202:
#             return 1, None
#         else:
#             raise Exception

#     except Exception as err:
#         message = {
#             'origin': origin,
#             'to': to,
#             'subject': subject,
#             'error_message': str(err),
#         }
#         send_err_by_email("ERROR trying send_email: ", str(message))

#     return 0, message