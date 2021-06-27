from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from postings.models   import JobPosting

class JobListView(View):

    def get(self, request):
        try:
            job_group = request.GET.get('job_group')
            tag       = request.GET.get('tag')
            nation    = request.GET.get('nation')
            career    = request.GET.get('career')
            sort_type = request.GET.get('sort_type')
            
            job_posting_filter = Q()

            if job_group:
                job_posting_filter.add((
                    Q(job_group__id = job_group)
                    ), Q.AND)
            
            if tag:
                job_posting_filter.add((
                    Q(company__tag__id = tag)
                    ), Q.AND)

            if nation:
                job_posting_filter.add((
                    Q(company__nation__id = nation)
                    ), Q.AND)

            if career:
                job_posting_filter.add((
                    Q(career__id = career)
                    ), Q.AND)

            job_posting_list = JobPosting.objects.filter(job_posting_filter).distinct()
            
            sort_lists = {
                '1' : '-created_at',
                '2' : '-like',
                '3' : '-award',
                '4' : '-reply',
            }

            if sort_type:
                job_posting_list = job_posting_list.order_by(sort_lists[sort_type])

            results = [{
                'id'                : job_posting.id,
                'job_posting_image' : str(job_posting.jobpostingimage_set.all().first()),
                'title'             : job_posting.title,
                'company'           : job_posting.company.name,
                'nation'            : job_posting.company.nation.name,
                'region'            : job_posting.company.region.name,
                'tag'               : [tag.name for tag in job_posting.company.tag.all()],
                'description'       : job_posting.description,
                'deadline'          : job_posting.deadline,
                'address'           : job_posting.company.address,
                'longitude'         : job_posting.company.longitude,
                'latitude'          : job_posting.company.latitude
            }for job_posting in job_posting_list]

            return JsonResponse({'MESSAGE':'SUCCESS', 'results':results}, status = 200)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)

        except ValueError:
            return JsonResponse({'MESSAGE':'VALUE_ERROR'}, status = 400)