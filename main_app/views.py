from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Card, Set
from .forms import FormatForm

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
    # get the sets the card doesn't have
    sets_card_doesnt_have = Set.objects.exclude(id__in = card.sets.all().values_list('id'))
    # instantiate FormatForm to be rendered in the template
    format_form = FormatForm()
    return render(request, 'cards/detail.html', { 
        # pass the card and format_form as context
        'card': card, 'format_form': format_form, 'sets': sets_card_doesnt_have,
        })

def assoc_set(request, card_id, set_id):
    Card.objects.get(id=card_id).sets.add(set_id)
    return redirect('detail', card_id=card_id)

def remove_set(request, card_id, set_id):
    Card.objects.get(id=card_id).sets.remove(set_id)
    return redirect('detail', card_id=card_id)
    
def add_format(request, card_id):
    # create the ModelForm using the data in the request.POST
    form = FormatForm(request.POST)
    # validate the form
    if form.is_valid():
        # dont save the form to the db until is had the card_id assigned
        new_format = form.save(commit=False)
        new_format.card_id = card_id
        new_format.save()
    return redirect('detail', card_id=card_id)

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