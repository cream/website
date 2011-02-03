from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<path>.*)', 
        'doc.views.view',
        name = 'blog_entry_details')
)
