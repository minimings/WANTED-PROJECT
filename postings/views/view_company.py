import json

from django.views import View
from django.http  import JsonResponse
from django.db    import transaction

from postings.models import (
                              Company, 
                              WebsiteAddress, 
                              NewsKeyword, 
                              Nation,
                              Region,
                              JobGroup,
                              Employee,
                              Establishment,
                              )
from users.utils     import login_decorator
from postings.utils  import (
                              validate_company_registration_number, 
                              validate_investment_amount
                              )

class CompanyView(View):
    @transaction.atomic
    @login_decorator
    def post(self, request):
        try:
            data                        = json.loads(request.body)
            company_user_id             = request.user.id
            name                        = data['name']
            address                     = data['address']
            company_registration_number = data['company_registration_number']
            investment_amount           = data['investment_amount']
            description                 = data['description']
            nation_id                   = data['nation_id']
            region_id                   = data['region_id']
            employees_id                = data['employees_id']
            job_group_id                = data['job_group_id']
            establishment_id            = data['establishment_id']
            website_address             = data.get('website_address')
            subscription_path           = data.get('subscription_path')
            news_keywords               = data.get('news_keyword')

            if not validate_company_registration_number:
                return JsonResponse({'MESSAGE':'INVALID_COMPANY_REGISTRATION_NUMBER'}, status = 400)

            if not validate_investment_amount:
                return JsonResponse({'MESSAGE':'INVALID_INVESTMENT_AMOUNT'}, status = 400)

            company, updated = Company.objects.update_or_create(
                name = name,
                defaults = {'company_user_id'             : company_user_id,
                            'address'                     : address,
                            'company_registration_number' : company_registration_number,
                            'investment_amount'           : investment_amount,
                            'description'                 : description,
                            'nation_id'                   : nation_id,
                            'region_id'                   : region_id,
                            'employees_id'                : employees_id,
                            'job_group_id'                : job_group_id,
                            'establishment_id'            : establishment_id,
                            'subscription_path'           : subscription_path,
                            }
                        )

            if website_address:
                WebsiteAddress.objects.bulk_create(
                    [WebsiteAddress(company = company, website_address = website) for website in website_address]
                )
                
            if news_keywords:
                for keyword in news_keywords:
                    news_keyword_id, created = NewsKeyword.objects.get_or_create(keyword = keyword)
                    company.company_news_keyword.add(news_keyword_id.id)

            return JsonResponse({'MESSAGE':'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)

    @login_decorator
    def get(self, request):
        user = request.user

        results = [{
            'user_email'           : user.email,
            'user_country_code'    : user.country_code.code,
            'user_phone_number'    : user.phone_number,
            'nation'               : [nation.name for nation in Nation.objects.all()],
            'region' : [{
                'region_id' : region.nation_id, 
                'name'      : region.name
                }for region in Region.objects.all()],
            'job_group'            : [job_group.name for job_group in JobGroup.objects.all()],
            'employee'             : [employee.employee for employee in Employee.objects.all()],
            'establishment'        : [establishment.establishment for establishment in Establishment.objects.all()]
        }]

        return JsonResponse({'MESSAGE':'SUCCESS', 'results':results}, status = 200)