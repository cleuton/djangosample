from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_recado>/', views.detalhe, name='detalhe'),
    path('excluir/<int:id_recado>/', views.excluir, name='excluir'),
    path('form_incluir/', views.form_incluir, name='form_incluir'),
    path('incluir/', views.incluir, name='incluir')
]