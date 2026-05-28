from django.shortcuts import render, redirect
from .forms import DescriptionForm
from .models import Description

# Create your views here.
def add_description(request):
    template_name = 'descriptions/add_description.html'
    context = {}
    if request.method == 'POST':
        form = DescriptionForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
    form = DescriptionForm()
    context['form'] = form
    return render(request, template_name, context)
