from django.conf.urls import url

from .views import get_tasks, add_task, edit_task, task_detail, toggle_status

urlpatterns = [
    url(r'^$', get_tasks, name='get_tasks'),
    url(r'^add/$', add_task, name='add_task'),
    url(r'^(?P<id>\d+)$', task_detail, name='task_detail'),
    url(r'^(?P<id>\d+)/edit/$', edit_task, name='edit_task'),
    url(r'^(?P<id>\d+)/toggle/$', toggle_status, name='toggle_status')
]
