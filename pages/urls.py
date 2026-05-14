from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageListView.as_view(), name='pages_list'),
    path('<int:pk>/', views.PageDetailView.as_view(), name='pages_detail'),
    path('crear/', views.PageCreateView.as_view(), name='pages_create'),
    path('<int:pk>/editar/', views.PageUpdateView.as_view(), name='pages_update'),
    path('<int:pk>/borrar/', views.PageDeleteView.as_view(), name='pages_delete'),
]
