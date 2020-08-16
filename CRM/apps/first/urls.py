from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.Base.as_view(), name='BaseView'),

    path('Record/', views.RecordListView.as_view(), name='RecordListView'),
    path('Record/<int:pk>/', views.RecordDetailView.as_view(), name='RecordDetailView'),
    path('Project', views.ProjectListView.as_view(), name='ProjectListView'),
    path('Interaction', views.InteractionFilterView.as_view(), name='InteractionFilterView'),
    path('Interaction/<int:pk>/', views.InteractionDetailView.as_view(), name='InteractionDetailView'),

    path('Create/CompanyAddress/', views.CompanyAddressCreate.as_view(), name='CompanyAddressCreate'),
    path('Create/Descriptin/', views.DescriptinCreate.as_view(), name='DescriptinCreate'),
    path('Create/Record/', views.RecordCreate.as_view(), name='RecordCreate'),
    path('Create/Project/', views.ProjectCreate.as_view(), name='ProjectCreate'),
    path('Create/Communication/', views.CommunicationCreate.as_view(), name='CommunicationCreate'),
    path('Create/Interaction/', views.InteractionCreate.as_view(), name='InteractionCreate'),
]