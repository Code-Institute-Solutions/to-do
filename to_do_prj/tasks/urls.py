from django.conf.urls import url
from tasks.views import get_tasks, task_detail, add_task, edit_task, update_status

urlpatterns = [
    url(r'^$', get_tasks, name='get_tasks'),
    url(r'^add$', add_task),
    url(r'^(?P<id>\d+)/edit$', edit_task, name='edit_task'),
    url(r'^(?P<id>\d+)', task_detail, name='task_detail'),
    url(r'^update/(?P<id>\d+)$', update_status, name='update_status')
]
