from django.urls import path
from contacts import views

urlpatterns = [
    path('', views.ContactListView.as_view(), name='contact_list'),
    path('<int:pk>/', views.ContactDetailView.as_view(), name='contact_detail'),
    path('add/', views.AddContactView.as_view(), name='add_contact'),
]
