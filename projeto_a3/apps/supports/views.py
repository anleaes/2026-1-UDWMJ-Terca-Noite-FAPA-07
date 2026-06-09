from django.shortcuts import render, get_object_or_404, redirect
from .forms import SupportForm
from .models import Support

# Create your views here.
def add_support(request):
    template_name = 'supports/add_support.html'
    context = {}
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('supports:list_supports')
    form = SupportForm()
    context['form'] = form
    return render(request, template_name, context)

def list_supports(request):
    template_name = 'supports/list_supports.html'
    supports = Support.objects.filter()
    context = {
        'supports': supports,
    }
    return render(request, template_name, context)

def edit_support(request, id_support):
    template_name = 'supports/add_support.html'
    context ={}
    support = get_object_or_404(Support, id=id_support)
    if request.method == 'POST':
        form = SupportForm(request.POST, instance=support)
        if form.is_valid():
            form.save()
            return redirect('supports:list_supports')
    form = SupportForm(instance=support)
    context['form'] = form
    return render(request, template_name, context)

def delete_support(request, id_support):
    support = Support.objects.get(id=id_support)
    support.delete()
    return redirect('supports:list_supports')
