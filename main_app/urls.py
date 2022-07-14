from django.urls import path
from . import views

urlpatterns = [
    # home route
    path('', views.home, name='home'),
    # about route
    path('about/', views.about, name='about'),
    # index route
    path('cards/', views.cards_index, name='index'),
    # detail route
    path('cards/<int:card_id>', views.cards_detail, name='detail'),
]
