from django.core.mail import send_mail
from forum.celery import app


@app.task
def send_activation_email(email, activation_code):
    activation_url = f'http://localhost:8000/api/v1/account/activate/{activation_code}'
    message = f'''
                Thank u for signing up.
                Please, activate your account
                Activation ling: {activation_url}
                '''
    send_mail(
        'Activate your account',
        message,
        'test@forum.kg',
        [email, ],
        fail_silently=False

    )
