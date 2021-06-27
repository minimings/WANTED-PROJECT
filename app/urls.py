from django.urls    import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('users', include('users.urls')),
    path('postings', include('postings.urls')),
    path('resumes', include('resumes.urls')),
    path('recommendations', include('recommendations.urls')),
]