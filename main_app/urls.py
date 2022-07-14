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
    # route for adding a Format
    path('cards/<int:card_id>/add_format/', views.add_format, name='add_format'),
    # route for seeing all sets
    path('sets/', views.SetList.as_view(), name='sets_index'),
    # route for inspecting a specific set
    path('sets/<int:pk>/', views.SetDetail.as_view(), name='sets_detail'),
    # route to create a set
    path('sets/create/', views.SetCreate.as_view(), name='sets_create'),
    # route to update a set
    path('sets/<int:pk>/update/', views.SetUpdate.as_view(), name='sets_update'),
    # route to delete a set
    path('sets/<int:pk>/delete/', views.SetDelete.as_view(), name='sets_delete'),
]
