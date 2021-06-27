import boto3

from django.views import View
from django.http  import JsonResponse
from django.db    import transaction

from resumes.models    import FileResume
from users.utils       import login_decorator
from app.settings.base import (AWS_ACCESS_KEY_ID, 
                               AWS_SECRET_ACCESS_KEY, 
                               AWS_STORAGE_BUCKET_NAME, 
                               AWS_REGION)

class FileResumeView(View):
    @transaction.atomic
    @login_decorator
    def post(self, request):
        try:
            file_resume  = request.FILES.getlist('file_resume')
            general_user = request.user

            if file_resume.content_type != 'application/pdf':
                return JsonResponse({'MESSAGE':'INVALID_FILE_TYPE'}, status = 400)
            
            s3_client = boto3.client(
                's3',
                aws_access_key_id     = AWS_ACCESS_KEY_ID,
                aws_secret_access_key = AWS_SECRET_ACCESS_KEY
                )

            s3_client.upload_fileobj(
                file_resume,
                AWS_STORAGE_BUCKET_NAME,
                file_resume.name,
                ExtraArgs = {
                    "ContentType" : file_resume.content_type
                }
            )

            FileResume.objects.create(
                general_user = general_user,
                file_resume  = f'https://wanted.s3.ap-northeast-2.amazonaws.com/{file_resume.name}',
                title        = file_resume.name
            )

            return JsonResponse({'MESSAGE':'SUCCESS'}, status = 200)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)

    @login_decorator
    def get(self, request, id):

        file_resume = FileResume.objects.filter(id = id)

        if not FileResume.objects.filter(id = id).exists():
            return JsonResponse({'MESSAGE':'RESUME_DOES_NOT_EXISTS'}, status = 404)

        s3_client = boto3.client(
            's3',
            aws_access_key_id     = AWS_ACCESS_KEY_ID,
            aws_secret_access_key = AWS_SECRET_ACCESS_KEY
            )

        file = s3_client.download_fileobj(
            AWS_STORAGE_BUCKET_NAME,
            file_name = f'Downloads/{file_resume}',
            key = f'{file_resume}'
        )

        return JsonResponse({'MESSAGE':'SUCCESS', 'file':file}, status = 200)

    @login_decorator
    def delete(self, request, id):
        FileResume.objects.get(
            general_user = request.user,
            id = id,
        )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status = 204)