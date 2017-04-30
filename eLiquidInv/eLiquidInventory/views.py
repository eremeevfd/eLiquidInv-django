from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404
from .models import *


def index(request):
    eLiquids = ELiquid.objects.all()
    context = {
        'eLiquids': eLiquids,
    }
    return render(request, 'eLiquidInventory/index.html', context)


def eliquid(request, eliquid_id):
    eLiquid = get_object_or_404(ELiquid, id=eliquid_id)
    compositions = get_list_or_404(Composition, eLiquid_id=eliquid_id)
    context = {
        'composition': compositions,
        'eLiquid': eLiquid,
    }
    return render(request, 'eLiquidInventory/composition.html', context)
