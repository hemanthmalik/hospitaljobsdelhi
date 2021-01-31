from django.core.mail import EmailMessage

def send_custom_mail(data):
    email = EmailMessage(
        data.first_name,
        data.email,
        'alokmalikk@gmail.com',
        ['hemantmalik121@gmail.com'],
        ['hemant.malik@etmedialabs.com'],
        reply_to=['hemantmalik121@gmail.com'],
        headers={'Message-ID': 'foo'},
    )
    email.attach_file(data.resume.path)
    email.send()