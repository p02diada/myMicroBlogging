from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from app_myMicroBlogging.views import inicio, buscar

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myMicroBlogging.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^$', inicio, name='index'),
    url(r'^buscar/$', buscar, name='buscar'),
    url(r'^app/', include('app_myMicroBlogging.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
