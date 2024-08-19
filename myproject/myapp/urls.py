from django.urls import path
from myapp.views import NamespaceStatusListView
from . import views

urlpatterns = [
    path('api/namespace-status/', NamespaceStatusListView.as_view(), name='namespace-status-list'),
    path('api/delete-namespace/', views.delete_namespace, name='delete_namespace'),
]