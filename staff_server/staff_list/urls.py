from django.urls import path

from .views import get_staff, AddStaff, SubstationDetailView, SubststionUpdateView, deleteStaff, login, logout, register

urlpatterns = [
    path('', get_staff, name='staff_list'),
    path('substation/<int:pk>/', SubstationDetailView.as_view(), name='detail'),
    path('staff/<int:pk>/', deleteStaff, name='delete'),
    path('staff/update/<int:pk>/', SubststionUpdateView.as_view(), name='update'),
    path('add/', AddStaff.as_view(), name='add_staff'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
]
