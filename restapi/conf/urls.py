from django.urls import path, include
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('api/', include('app.urls')),
    path('doc/', include_docs_urls(title='Field API')),
]
