import json
import boto3

from django.views     import View
from django.http      import JsonResponse
from django.db        import transaction

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
            career_id         = data['career_id']
            job_group_id      = data['job_group_id']
            job_posting_image = request.FILES.getlist('job_posting_image')

            job_posting, updated = JobPosting.objects.update_or_create(
                company_id   = user.companyuser.company.id,
                title        = title,
                description  = description,
                deadline     = deadline,
                career_id    = career_id,
                job_group_id = job_group_id
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