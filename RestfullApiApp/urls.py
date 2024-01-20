from django.urls import path
from .views import Model1Lista, Model1Szczegoly

urlpatterns = [
    path('model1_lista/', Model1Lista.as_view(), name='Model1-lista'),
    path('model1_szczegoly/<int:pk>/', Model1Szczegoly.as_view(), name='Model1-szczegoly'),
]