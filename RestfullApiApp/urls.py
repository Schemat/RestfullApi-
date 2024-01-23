from django.urls import path
from .views import AuthorList, AuthorDetails

# TODO: Use meaningful model and field names
urlpatterns = [
    path('model1_lista/', AuthorList.as_view(), name='Model1-lista'),
    path('model1_szczegoly/<int:pk>/', AuthorDetails.as_view(), name='Model1-szczegoly'),
]
