# views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .decorators import group_required
from .forms import ProduccionDiariaForm
from .models import ProduccionDiaria
#api
from rest_framework import viewsets
from .serializer import ProduccionDiariaSerializer
#filtro
from .filters import ProduccionDiariaFilter
from django_filters import rest_framework as filters


@login_required
@group_required('Operador')
def panel_operador_view(request):
    return render(request, 'operador.html')

def inicio(request):
    return render(request,'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('panel')  # Redirige a la página de registro después de iniciar sesión
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'login.html')

@login_required
@group_required('Operador')
def registro_view(request):
    if request.method == 'POST':
        form = ProduccionDiariaForm(request.POST)
        if form.is_valid():
            produccion = form.save(commit=False)
            produccion.operador = request.user
            produccion.save()
            return redirect('panel')  # Redirige a la página principal del operador
    else:
        form = ProduccionDiariaForm()
    
    is_operador = request.user.groups.filter(name='Operador').exists()
    return render(request, 'registro.html', {'form': form, 'is_operador': is_operador})


def access_denied_view(request):
    return render(request, 'access_denied.html')




@login_required
@group_required('Operador')
def lista_producciones_view(request):
    filtro = request.GET.get('filtro', 'mis')
    if filtro == 'todas':
        producciones = ProduccionDiaria.objects.all()
    else:
        producciones = ProduccionDiaria.objects.filter(operador=request.user)

    return render(request, 'lista_producciones.html', {'producciones': producciones, 'filtro': filtro})

@login_required
@group_required('Operador')
def editar_produccion_view(request, pk):
    produccion = get_object_or_404(ProduccionDiaria, pk=pk, operador=request.user)
    if request.method == 'POST':
        form = ProduccionDiariaForm(request.POST, instance=produccion)
        if form.is_valid():
            form.save()
            return redirect('lista_producciones')
    else:
        form = ProduccionDiariaForm(instance=produccion)
    return render(request, 'editar_produccion.html', {'form': form})

class ProduccionDiariaViewSet(viewsets.ModelViewSet):
    queryset=ProduccionDiaria.objects.all()
    serializer_class=ProduccionDiariaSerializer
    filter_backends=(filters.DjangoFilterBackend,)
    filterset_class = ProduccionDiariaFilter