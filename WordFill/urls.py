from django.conf.urls.defaults import *
from WordFill.index import request_word

urlpatterns = patterns('',
 (r'^query/([A-Za-z]{1,20})/$', request_word)
)