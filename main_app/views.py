from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Card, Set
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', { 'cards': cards})

def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    return render(request, 'cards/detail.html', { 
        'card': card,
        })

class CardCreate(CreateView):
    model = Card
    fields = '__all__'
    success_url = '/cards/'

class CardUpdate(UpdateView):
    model = Card
    fields = ['type', 'description', 'power', 'toughness']

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards/'

####################
## Set Views
####################
class SetList(ListView):
  model = Set

class SetDetail(DetailView):
  model = Set

class SetCreate(CreateView):
  model = Set
  fields = '__all__'
  success_url = '/sets/'

class SetUpdate(UpdateView):
  model = Set
  fields = '__all__'

class SetDelete(DeleteView):
  model = Set
  success_url = '/sets/'