from django.shortcuts import render
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.http import HttpResponse

# import sendgrid
# from sendgrid.helpers.mail import Email, Content, Mail, CustomArg


def home(request):
    return render(request, 'web/login.html', locals())


def invite_user(request):
    print('ya tengo el poder!')
    if request.method == 'POST':
        email = EmailMessage(
            'Hello',
            'Body goes here',
            'javier@atixplus.com',
            ['bichocj@gmail.com'],
            [],
            reply_to=['another@gmail.com'],
            headers={'Message-ID': 'bichocj@gmail.com'},
        )
        print('emailllllllllllll.send()')
        print(email.send())

    return render(request, 'web/er/users/form.html', locals())


@csrf_exempt
@require_POST
def sendgrid_webhook(request):
    if request.method == 'POST':
        response = json.loads(request.body)
        print(response)

        # if len(response) > 1:
        #     event = response[1]
        # else:
        #     event = response[0]

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