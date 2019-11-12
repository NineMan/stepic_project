from django.conf.urls import url
from qa.views import test, main, popular, question


urlpatterns = (
    url(r'^$', main, name='index'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='signup'),
    url(r'^question/(?P<question_id>[0-9]+)/$', question, name='question'),
    url(r'^ask/', test, name='ask'),
    url(r'^answer/', test, name='answer'),
    url(r'^popular/', popular, name='popular'),
    url(r'^new/', test, name='new'),
)

