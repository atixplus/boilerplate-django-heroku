from django.shortcuts import render
from django.core.mail import EmailMessage

def home(request):
    return render(request, 'web/login.html', locals())

def invite_user(request):
    print('ya tengo el poder!')
    if request.method == 'POST':
        email = EmailMessage(
            'Hello',
            'Body goes here',
            'from@example.com',
            ['to1@example.com', 'to2@example.com'],
            ['bcc@example.com'],
            reply_to=['another@example.com'],
            headers={'Message-ID': 'foo'},
        )
        print('emailllllllllllll.send()')
        print(email.send())

    return render(request, 'web/er/users/form.html', locals())
