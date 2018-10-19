from django.conf.urls import url
from django.contrib import admin
from studentInfo import views
from studentInfo.models import Student
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url pattern to make get and post request
    url(r'^student/(?P<name>[\w-]+)/$', views.StudentList.as_view()),

]
