from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Card, Set, Photo
from .forms import FormatForm

S3_BASE_URL = 'https://s3.us-west-2.amazonaws.com/'
BUCKET = 'mtgcollector-karc-90'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def cards_index(request):
    cards = Card.objects.filter(user=request.user)
    return render(request, 'cards/index.html', { 'cards': cards})

@login_required
def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id, user=request.user)
    if not card.user == request.user:
        return redirect('home')
    # get the sets the card doesn't have
    sets_card_doesnt_have = Set.objects.exclude(id__in = card.sets.all().values_list('id'))
    # instantiate FormatForm to be rendered in the template
    format_form = FormatForm()
    return render(request, 'cards/detail.html', { 
        # pass the card and format_form as context
        'card': card, 'format_form': format_form, 'sets': sets_card_doesnt_have,
        })

@login_required
def assoc_set(request, card_id, set_id):
    card = Card.objects.get(id=card_id, user=request.user)
    if not card.user == request.user:
        return redirect('home')
    card.sets.add(set_id)
    return redirect('detail', card_id=card_id)


@login_required
def remove_set(request, card_id, set_id):
    card = Card.objects.get(id=card_id, user=request.user)
    if not card.user == request.user:
        return redirect('home')
    card.sets.remove(set_id)
    return redirect('detail', card_id=card_id)


@login_required
def add_format(request, card_id):
    card = Card.objects.get(id=card_id, user=request.user)
    if not card.user == request.user:
        return redirect('home')
    # create the ModelForm using the data in the request.POST
    form = FormatForm(request.POST)
    # validate the form
    if form.is_valid():
        # dont save the form to the db until is had the card_id assigned
        new_format = form.save(commit=False)
        new_format.card_id = card_id
        new_format.save()
    return redirect('detail', card_id=card_id)

@login_required
def add_photo(request, card_id):
    card = Card.objects.get(id=card_id, user=request.user)
    if not card.user == request.user:
        return redirect('home')
    # photo-file will be the 'name' attribute on the <input type='file'>
    photo_file = request.FILES.get('photo-file', None)
    print(f"this is photo_file -->> {photo_file}")
    if photo_file:
        s3 = boto3.client('s3')
        print(f"this is s3 -->> {s3}")
        # need a unique 'key for s3 / needs file extension
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        print(f"this is key -->> {key}")
        # error handling
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, card_id=card_id)
            print(f"this is photo in try block -->> {photo}")
            photo.save()
        except:
            print('An error occured')
    return redirect('detail', card_id=card_id)

def signup(request):
    error_message = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
        
class CardCreate(LoginRequiredMixin, CreateView):
    model = Card
    fields = ['name', 'type', 'power', 'toughness', 'description']

    def form_valid(self, form):
        # assign the logged in user (self.request.user)
        form.instance.user = self.request.user
        return super().form_valid(form)

class CardUpdate(LoginRequiredMixin, UpdateView):
    model = Card
    fields = ['name', 'type', 'description', 'power', 'toughness']

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        card = super(CardUpdate, self).get_object()
        if not card.user == self.request.user:
            return redirect('home')
        return card

class CardDelete(LoginRequiredMixin, DeleteView):
    model = Card
    success_url = '/cards/'

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        card = super(CardUpdate, self).get_object()
        if not card.user == self.request.user:
            return redirect('home')
        return card

####################
## Set Views
####################
class SetList(LoginRequiredMixin, ListView):
  model = Set

class SetDetail(LoginRequiredMixin, DetailView):
  model = Set

class SetCreate(LoginRequiredMixin, CreateView):
  model = Set
  fields = '__all__'
  success_url = '/sets/'

class SetUpdate(LoginRequiredMixin, UpdateView):
  model = Set
  fields = '__all__'

class SetDelete(LoginRequiredMixin, DeleteView):
  model = Set
  success_url = '/sets/'