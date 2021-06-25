import re
import jwt

from django.http import JsonResponse

from users.models      import User
from app.settings.base import SECRET_KEY, ALGORITHM

def validate_email(email):
    email_form = re.comfile('^[a-zA-Z0-9+-_.]+@[a-z]+\.[a-z]+$')
    return email_form.match(email)

def validate_name(name):
    name_form = re.comfile('^(?=.*\w)(?!.*?\W)(\S)*$')
    return name_form.match(name)

def validate_phone_number(phone_number):
    phone_number_form = re.compile('^01([0|1|6|7|8|9]?)([0-9]{3,4})([0-9]{4})$')
    return phone_number_form.match(phone_number)

def validate_password(password):
    password_form = re.compile('^(?=.*[A-Za-z])(?=.*\d)(\S){10,}$')
    return password_form.match(password)

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token        = request.headers.get('Authorization', None)
            payload      = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
            user         = User.objects.get(id=payload['id'])
            request.user = user
            return func(self, request, *args, **kwargs)
        except jwt.exceptions.DecodeError:
            return JsonResponse({'MESSAGE':'INVALID_TOKEN'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=400)
    
    return wrapper