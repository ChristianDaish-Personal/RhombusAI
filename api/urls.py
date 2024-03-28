from django.urls import include,path
# from .views import ItemListCreate, ItemDetail, FileUploadView
from .views import FileUploadView

from dataprocessor.views import your_view


urlpatterns = [
    # path('items/', ItemListCreate.as_view(), name='item-list'),
    # path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
    path('view-data/', your_view,name='view_data'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
]