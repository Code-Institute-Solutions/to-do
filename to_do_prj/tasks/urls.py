from django.conf.urls import url
from tasks.views import get_tasks, add_task

urlpatterns = [
    url(r'^$', get_tasks),
    url(r'^add$', add_task)
]