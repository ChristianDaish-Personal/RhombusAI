from django.urls import include,path
from .views import your_view

urlpatterns = [
    path('process/', your_view, name='process_files'),
]
