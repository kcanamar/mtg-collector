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
    # route for adding a Format 1:M
    path('cards/<int:card_id>/add_format/', views.add_format, name='add_format'),
    # route for adding a photo
    path('cards/<int:card_id>/add_photo/', views.add_photo, name='add_photo'),
    # route for associating a set to a card M:M
    path('cards/<int:card_id>/assoc_set/<int:set_id>/', views.assoc_set, name='assoc_set'),
    # route for removing a set from a card
    path('cards/<int:card_id>/remove_set/<int:set_id>/', views.remove_set, name='remove_set'),
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
    # signup route
    path('accounts/signup/', views.signup, name='signup'),
]
