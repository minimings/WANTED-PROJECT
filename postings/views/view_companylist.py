from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from postings.models import Company, TagCategory, Tag

class CompanyListView(View):
    def get(self, request):
        tag = request.GET.get('tag')
        search = request.GET.get('search')

        company_filter = Q()

        if tag:
            company_filter(
                (Q(tag__id = tag)
                ), Q.AND)

        company_list = Company.objects.filter(company_filter).distinct()

        if search:
            company_list = Company.objects.filter(name__icontains = search)

        tags = [{
            'tag_category' : category.name,
            'tags' : [{
                'id'   : tag.id,
                'name' : tag.name
            }for tag in Tag.objects.all()]
        }for category in TagCategory.objects.all()]

        results = [{
            'icon'      : str(company.icon),
            'name'      : company.name,
            'job_group' : company.job_group.name,
            'is_follow' : [follow.is_follow for follow in company.follow_set.filter(general_user = request.user.id)],
            'tag'       : [tag.name for tag in company.tag.all()]
        }for company in company_list]

        return JsonResponse({'MESSAGE':'SUCCESS', 'tags':tags, 'results':results}, status = 200)