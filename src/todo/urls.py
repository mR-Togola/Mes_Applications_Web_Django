from django.urls import path
from .views import index, add_collections, add_taches, get_taches


urlpatterns = [
   
    path('', index, name='home_todo'),
    path('add_taches', add_taches, name='add_taches'),
    path('get_taches/<int:collection_pk>', get_taches, name='get_taches'),

    path('add-collection/', add_collections, name='collections_taches'),
    ]