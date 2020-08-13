from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.Base.as_view(), name='BaseView'),
    path('Record/', views.RecordListView.as_view(), name='RecordListView'),
    path('Record/<int:pk>/', views.RecordDetailView.as_view(), name='RecordDetailView'),
    path('post/new/', views.PostRecordAdd, name='PostRecordAdd'),
    # path('post/<int:pk>/edit/', views.PostRecordEdit, name='PostRecordEdit'),
    path('Project', views.ProjectListView.as_view(), name='ProjectListView'),
    path('Interaction/', views.InteractionListView.as_view(), name='InteractionListView'),
    path('Interaction/<int:pk>/', views.InteractionDetailView.as_view(), name='InteractionDetailView'),
    # path('Interaction/<>/', views.InteractionFilterView.as_view(), name='InteractionFilterlView'),
]