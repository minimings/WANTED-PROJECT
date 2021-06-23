import json
import jwt
import bcrypt

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q
from django.db        import transaction

from app.settings.base import SECRET_KEY, ALGORITHM
from users.models      import User, GeneralUser, CompanyUser, University
from postings.models   import Company
from users.utils       import (
                                validate_email, 
                                validate_name, 
                                validate_password, 
                                validate_phone_number
                                )

class SignUpView(View):
    @transaction.atomic
    def post(self, request):
        try:
            data            = json.loads(request.body)
            email           = data['email']
            name            = data['name']
            phone_number    = data['phone_number']
            password        = data['password']
            is_social       = data.get('is_social', False)
            type            = data['type']
            country_code_id = data['country_code_id']

            if not validate_email:
                return JsonResponse({'MESSAGE':'INVALID_EMAIL'}, status = 400)

            if not validate_name:
                return JsonResponse({'MESSAGE':'INVALID_NAME'}, status = 400)

            if not validate_password:
                return JsonResponse({'MESSAGE':'INVALID_PASSWORD'}, status = 400)
            
            if not validate_phone_number:
                return JsonResponse({'MESSAGE':'INVALID_PHONE_NUMBER'}, status = 400)

            if not (type == '일반회원' or type == '기업회원'):
                return JsonResponse({'MESSAGE':'INVALID_TYPE'}, status = 400)

            if User.objects.filter(
                Q(email        = email) |
                Q(phone_number = phone_number)
            ).exists():
                return JsonResponse({'MESSAGE':'ALREADY_EXISTS'}, status = 400)

            password        = data['password'].encode('utf-8')
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            hashed_password = hashed_password.decode('utf-8')

            user = User.objects.create(
                email           = email,
                name            = name,
                phone_number    = phone_number,
                password        = hashed_password,
                is_social       = is_social,
                type            = type,
                country_code_id = country_code_id,
            )

            if type == '일반회원':
                is_subscribe          = data.get('is_subscribe', False)
                career_id             = data.get('career_id')
                job_group_id          = data.get('job_group_id')
                worry_id              = data.get('worry_id')
                interested_keyword_id = data.get('interested_keyword_id')
                user_company          = data.get('user_company')
                user_university       = data.get('user_university')

                general_user = GeneralUser.objects.create(
                    is_subscribe = is_subscribe,
                    career_id    = career_id,
                    job_group_id = job_group_id,
                    worry_id     = worry_id,
                    user         = user,
                )

                if interested_keyword_id:
                    [general_user.interested_keyword.add(id) for id in interested_keyword_id]

                if user_company:
                    if not Company.objects.filter(name = user_company).exists():
                        return JsonResponse({'MESSAGE':'COMPANY_DOES_NOT_EXISTS'}, status = 400)
                    company_id = Company.objects.get(name = user_company).id
                    general_user.user_company.add(company_id)

                if user_university:
                    if not University.objects.filter(name = user_university).exists():
                        return JsonResponse({'MESSAGE':'UNIVERSITY_DOES_NOT_EXISTS'}, status = 400)
                    university_id = University.objects.get(name = user_university).id
                    general_user.user_university.add(university_id)

                return JsonResponse({'MESSAGE':'SUCCESS'}, status = 201)

            if type == '기업회원':
                position = data['position']

                CompanyUser.objects.create(
                    position = position,
                    user     = user
                )
                
                return JsonResponse({'MESSAGE':'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)

class SignInView(View):
    def post(self, request):
        data     = json.loads(request.body)
        email    = data['email']
        password = data['password']

        if user := User.objects.filter(email = email):
            if bcrypt.checkpw(password.encode('utf-8'), user.get().password.encode('utf-8')):
                token = jwt.encode({'id' : user.get().id}, SECRET_KEY, algorithm=ALGORITHM)
                return JsonResponse({'MESSAGE':'SUCCESS', 'TOKEN':token, 'name':user.name}, status = 200)
            return JsonResponse({'MESSAGE':'PASSWORD_ERROR'}, status = 401)
        return JsonResponse({'MESSAGE':'INVALID_USER'}, status = 404)