from django.shortcuts import render
from .models import *
from .forms import *
import requests


# Create your views here.

def index(request):
    url = 'https://pokeapi.co/api/v2/pokemon/{}'
    pokemon = 'rayquaza'

    err_msg = ''


    if request.method == 'POST':
        form = PokemonForm(request.POST)

        if form.is_valid():
            new_pokemon = form.cleaned_data['name']
            existing_pokemon_count = Pokemon.objects.filter(name=new_pokemon).count()

            if existing_pokemon_count == 0:
                r = requests.get(url.format(new_pokemon)).json()
                form.save()
        else:
            err_msg = 'Pokemon already existing'

    print(err_msg)

    form = PokemonForm()

    pokemons = Pokemon.objects.all()

    pokemon_data = []

    for pokemon in pokemons:

        r = requests.get(url.format(pokemon)).json()

        pokemon_info = {
            'name': pokemon.name,
            'height': r['height'],
            'weight': r['weight'],
            'types': r['types'][0]['type']['name'],
            'pic': r['sprites']['front_default']
        }

        pokemon_data.append(pokemon_info)

    context = {'pokemons': pokemon_data, 'form': form}

    return render(request, 'index.html',context)