from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, r'C:\Users\drusti\Desktop\Clase programacion\ProjectDjango2\mi_sitio\paginas\templates\paginas\inicio.html')

def contacto(request):
    return render(request, r'C:\Users\drusti\Desktop\Clase programacion\ProjectDjango2\mi_sitio\paginas\templates\paginas\contacto.html')

def acerca(request):
    return render(request, r'C:\Users\drusti\Desktop\Clase programacion\ProjectDjango2\mi_sitio\paginas\templates\paginas\acerca.html')
