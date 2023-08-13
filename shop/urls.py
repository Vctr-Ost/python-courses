from django.urls import path
from .views import index, single_course



urlpatterns = [
    path('', index, name='index'),
    path('<int:course_id>', single_course, name='single_course'),
]