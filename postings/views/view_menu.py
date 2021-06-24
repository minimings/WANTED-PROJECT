from django.views import View
from django.http  import JsonResponse

from postings.models import Menu

class MenuView(View):
    def get(self, request):
        results = [
            {
                'id'        : menu.id,
                'name'      : menu.name,
                'job_group' : [{
                    'id'   : job_group.id,
                    'name' : job_group.name
                }for job_group in menu.jobgroup_set.all()]
            }for menu in Menu.objects.all()]

        return JsonResponse({'MESSAGE':'SUCCESS', 'results':results}, status = 200)