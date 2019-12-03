from django.conf.urls import url
from qa.views import test, main, popular, question, ask, answer


urlpatterns = (
    url(r'^$', main, name='index'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='signup'),
    url(r'^question/(?P<question_id>[0-9]+)/$', question, name='question'),
    url(r'^ask/', ask, name='ask'),
    url(r'^answer/', answer, name='answer'),
    url(r'^popular/', popular, name='popular'),
    url(r'^new/', test, name='new'),
)

