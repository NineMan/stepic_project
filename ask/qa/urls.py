from django.conf.urls import url
from qa.views import test


urlpatterns = (
    url(r'^$', test, name='index'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='signup'),
    url(r'^question/(?P<quest_id>[0-9]+)/$', test, name='question'),
    url(r'^ask/', test, name='ask'),
    url(r'^answer/', test, name='answer'),
    url(r'^popular/', test, name='popular'),
    url(r'^new/', test, name='new'),
)

