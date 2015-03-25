from django.shortcuts import render
from models import Pages
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def mostrar(request, recurso):

    if request.method == "GET":
        try:
            clave = Pages.objects.get(name=recurso)
            return HttpResponse(clave.page)

        except Pages.DoesNotExist:
            return HttpResponseNotFound("Page not found")

    if request.method == "PUT":
        page = Pages(name=recurso, page=request.body)
        page.save()
        return HttpResponse("Contenido Guardado")
