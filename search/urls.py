from search.views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', index, name='index'),
                  path('hashtag.json', PostsJson.as_view()),
                  path("json-filter/", JsonFilter.as_view(), name='json_filter'),
                  path("post/<slug:slug>", post_page, name='post'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
