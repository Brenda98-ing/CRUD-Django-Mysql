from django.urls import path
from .views import TablasMysql

#Registro mi método de vistas en url, con los datos respectivos de mi ruta
#Así se ve la ruta http://127.0.0.1:8000/ejercicio/ PARA POST
urlpatterns = [
    path('ejercicio/', TablasMysql.as_view(), name='get_list'),
    path('ejercicio/<int:id>', TablasMysql.as_view(), name='get_list_id')
]