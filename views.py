from django.shortcuts import render, redirect, get_object_or_404
from .models import SDM
from .forms import SDMForm

def sdm_list(request):
    data = SDM.objects.all()
    return render(request, 'sdm/sdm_list.html', {'data': data})

def sdm_create(request):
    form = SDMForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sdm_list')
    return render(request, 'sdm/sdm_form.html', {'form': form})

def sdm_update(request, pk):
    sdm = get_object_or_404(SDM, pk=pk)
    form = SDMForm(request.POST or None, instance=sdm)
    if form.is_valid():
        form.save()
        return redirect('sdm_list')
    return render(request, 'sdm/sdm_form.html', {'form': form})

def sdm_delete(request, pk):
    sdm = get_object_or_404(SDM, pk=pk)
    if request.method == 'POST':
        sdm.delete()
        return redirect('sdm_list')
    return render(request, 'sdm/sdm_confirm_delete.html', {'sdm': sdm})
