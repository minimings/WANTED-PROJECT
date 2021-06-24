from django.urls    import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users', include('users.urls')),
    path('postings', include('postings.urls')),
    path('resumes', include('resumes.urls')),
    path('recommendations', include('recommendations.urls')),
    path('accounts/', include('allauth.urls')),
]