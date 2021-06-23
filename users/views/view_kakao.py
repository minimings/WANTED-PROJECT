import jwt
import requests

from django.views import View
from django.http  import JsonResponse

from app.settings.base import SECRET_KEY, ALGORITHM
from users.models      import User, GeneralUser, ProfileImage

class KakaoView(View):
    def post(self, request):
        try:
            access_token = request.headers.get('Authorization')
            url          = 'https://kapi.kakao.com/v2/user/me'
            headers      = {'Authorization': f'Bearer {access_token}',
                            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
            }

            response      = requests.get(url, headers = headers)
            data          = response.json()
            kakao_user_id = data['id']
            email         = data['kakao_account']['email']
            nickname      = data['kakao_account']['profile']['nickname']
            profile_image = data['kakao_account']['profile']['profile_image_url']

            if not User.objects.filter(kakao_user_id = kakao_user_id).exists():
                user = User.objects.create(
                    kakao_user_id = kakao_user_id,
                    email         = email,
                    name          = nickname,
                    is_social     = True,
                    social_id     = 1
                )

                GeneralUser.objects.create(
                    user          = user,
                    profile_image = ProfileImage.objects.create(profile_image = profile_image),
                    is_subscribe  = False
                )
            
            token = jwt.encode({'id': User.objects.get(kakao_user_id = kakao_user_id).id}, SECRET_KEY, algorithm = ALGORITHM)
            return JsonResponse({'TOKEN': token, 'name': nickname}, status = 200)

        except KeyError:
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status = 400)