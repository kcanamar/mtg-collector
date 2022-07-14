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
    # create route for card
    path('cards/create/', views.CardCreate.as_view(), name='cards_create'),
    # update route for card
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name='cards_update'),
    # delete route for card
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name='cards_delete'),
]
