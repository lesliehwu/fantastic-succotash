from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$', views.index),
        url(r'^add', views.add),
        url(r'^remove/(?P<course_id>\d+)', views.remove), #delete action
        url(r'^destroy/(?P<course_id>\d+)', views.destroy), #renders delete page
]
