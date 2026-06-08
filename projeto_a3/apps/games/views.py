from django.shortcuts import render, get_object_or_404, redirect
from .forms import GameForm
from .models import Game

# Create your views here.
def add_game(request):
    template_name = 'games/add_game.html'
    context = {}
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('games:list_games')
    form = GameForm()
    context['form'] = form
    return render(request, template_name, context)

def list_games(request):
    template_name = 'games/list_games.html'
    games = Game.objects.filter()
    context = {
        'games': games
    }
    return render(request, template_name, context)

def edit_game(request, id_game):
    template_name = 'games/add_game.html'
    context ={}
    game = get_object_or_404(Game, id=id_game)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES,  instance=game)
        if form.is_valid():
            form.save()
            return redirect('games:list_games')
    form = GameForm(instance=game)
    context['form'] = form
    return render(request, template_name, context)

def delete_game(request, id_game):
    game = Game.objects.get(id=id_game)
    game.delete()
    return redirect('games:list_games')
