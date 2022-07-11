from cgi import print_arguments
from django import views
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Tiposdispositivo,Dispositivo
import json

# Create your views here.
class TablasMysql(View):
    #Metodo que se sobreescribe
    #Metodo para se va mandar a llamar cada que se ejecute una peticion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
   
    
    #Path ---GET --- http://127.0.0.1:8000/ejercicio/2
    #Obtener datos de acuerdo a id
    def get(self,request,id=0):
        #Con el uso de ORM de Django vamos a importar nuestros modelos en variables
        #Primero trabajaremos con la tabla tiposDispositivos
        #El mapeo de ellos objetos relacional
        #Ruta http://127.0.0.1:8000/get/
        print(id)

        if (id>0):
            #Validamos que el id sea diferente a 0
            #Realizamos el respectivo filtro para solo tomar el id
            dispositivos=list(Dispositivo.objects.filter(dispositivo_id=id).values())
            
            if len(dispositivos)>0:
              #Si nuestra tabla tiene datos
              respuesta_dispositivo=dispositivos[0]
              mensaje={'message':"Success", 'TablaTiposDispositivos':respuesta_dispositivo}
            else:
              mensaje={'message':"Company not found.."}
            
            return JsonResponse(mensaje)

        else:
            #Convertimos nuestra info en lista para poder convertirlo a JSON
            Dispositivos=list(Dispositivo.objects.values())
            
            #Validamos que se este leyendo el modelo de la tabla
            if len(Dispositivos)>0:
                #si TablaTiposDispositivos esta lleno
                #Armamos json
                mensaje={'message':"Success", 'TablaTiposDispositivos':Dispositivos}
            else:
                mensaje={'message':"Companias no encontradas"}
                #En el return convierte el la lista a JSON
        return JsonResponse(mensaje)

    #Path ---POST --- http://127.0.0.1:8000/ejercicio/
    #Insertar datos
    def post(self,request):
        #print(request.body)
        #cargamos nuestro archivo json en una variable llamada response_JSON
        body=json.loads(request.body)
        #Solo para ver que datos van a ser insertados
        print(body)
        #Empezamos proceso para ingresar datos:
        #Mandamos a llamar a nuestra tabla Dispositivos y mencionamos cada campo de nuestra tabla
        Dispositivo.objects.create(nombre_de_equipo=body['nombre_de_equipo'], tiposdispositivo_id=body['tiposdispositivo_id'], fecha_de_alta=body['fecha_de_alta'], fecha_de_actualizacion=body['fecha_de_actualizacion'], potencia_actual=body['potencia_actual'], statusdispositivo_id=body['statusdispositivo_id'])

        dato={'message':"Success"}
        return JsonResponse(dato)

    #Path --- PUT --- http://127.0.0.1:8000/ejercicio/8
    #Modificar datos
    def put(self,request,id):
        #Cargamos los datos nuevos que se ingresaran
        body_new=json.loads(request.body)
        #Creamos el filtro
        dispositivo_filtro=list(Dispositivo.objects.filter(dispositivo_id=id).values())
        if len(dispositivo_filtro)>0:
            #Obtenemos los datos de acuerdo al id
            datos=Dispositivo.objects.get(dispositivo_id=id)
            #Empezamos a sustituirlos
            datos.nombre_de_equipo=body_new['nombre_de_equipo']
            datos.tiposdispositivo_id=body_new['tiposdispositivo_id']
            datos.fecha_de_alta=body_new['fecha_de_alta']
            datos.fecha_de_actualizacion=body_new['fecha_de_actualizacion']
            datos.potencia_actual=body_new['potencia_actual']
            datos.statusdispositivo_id=body_new['statusdispositivo_id']
            datos.save()
            mensaje={'message':"Success"}
        else:
            mensaje={'message':"Compania no encontrada"}
        return JsonResponse(mensaje)

    #Path --- DELETE --- http://127.0.0.1:8000/ejercicio/8
    #Eliminar dato de acuerdo a ID
    def delete(self,request,id):
        dispositivo_filtro=list(Dispositivo.objects.filter(dispositivo_id=id).values())
        #Realizamos el filtro para verificar si hay datos
        if len(dispositivo_filtro)>0:
            #Validamos si existe
            #Luego eliminamos las funciones del ORM de DJANGO
            Dispositivo.objects.filter(dispositivo_id=id).delete()
            mensaje={'message':"Success"}
        else:
            mensaje={'message':"No existee"}
        return JsonResponse(mensaje)


