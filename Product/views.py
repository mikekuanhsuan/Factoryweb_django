from django.shortcuts import redirect, render

from .models import Factory



def factory_list(request):
    factories = Factory.objects.all()
    return render(request, 'factory_list.html', {'factories': factories})

