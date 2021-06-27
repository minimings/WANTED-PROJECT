import json
import boto3

from django.views     import View
from django.http      import JsonResponse
from django.db        import transaction
from django.db.models import Q

from postings.models   import JobPosting, JobPostingImage
from users.utils       import login_decorator
from app.settings.base import (AWS_ACCESS_KEY_ID, 
                               AWS_SECRET_ACCESS_KEY, 
                               AWS_STORAGE_BUCKET_NAME)

class JobPostingView(View):
    @transaction.atomic
    @login_decorator
    def post(self, request):
        try:
            data              = json.loads(request.body)
            user              = request.user
            title             = data['title']
            description       = data['description']
            deadline          = data['deadline']
            job_posting_image = request.FILES.getlist('job_posting_image')

            job_posting, updated = JobPosting.objects.update_or_create(
                company_id  = user.companyuser.company.id,
                title       = title,
                description = description,
                deadline    = deadline,
            )

            s3_client = boto3.client(
                's3',
                aws_access_key_id     = AWS_ACCESS_KEY_ID,
                aws_secret_access_key = AWS_SECRET_ACCESS_KEY
                )

            for image in job_posting_image:
                s3_client.upload_fileobj(
                image,
                AWS_STORAGE_BUCKET_NAME,
                image.name,
                ExtraArgs = {
                    "ContentType" : image.content_type
                }
            )

            job_posting.jobpostingimage_set.bulk_create([
                JobPostingImage(
                    job_posting       = job_posting,
                    job_posting_image = f'https://wanted.s3.ap-northeast-2.amazonaws.com/{image.name}'
                    )for image in job_posting_image])
            
            return JsonResponse({'MESSAGE':'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)

    def get(self, request):
        try:
            job_group = request.GET.get('job_group')
            tag       = request.GET.get('tag')
            nation    = request.GET.get('nation')
            career    = request.GET.get('career')
            sort_type = request.GET.get('sort_type')
            
            job_posting_filter = Q()

            if job_group:
                job_posting_filter(
                    (Q(job_group__id = job_group)
                    ), Q.AND)
            
            if tag:
                job_posting_filter(
                    (Q(tag__id = tag)
                    ), Q.AND)

            if nation:
                job_posting_filter(
                    (Q(nation__id = nation)
                    ), Q.AND)

            if career:
                job_posting_filter((Q(career__id = career)
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