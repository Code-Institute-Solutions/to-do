from django.conf.urls import url
from tasks.views import get_tasks

urlpatterns = [
    url(r'^$', get_tasks)
]