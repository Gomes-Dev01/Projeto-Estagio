from django.urls import path
from  django.contrib.auth import views
from . import views
from .views import usuarios, niveisAcesso, cadastroTela, Telas, alteraNivel



urlpatterns = [
    path('', views.index, name='usuario-login'),
    path('usuario/', views.homeUsuario, name='usuario-home'),
    path('listagemUsuario/', usuarios.as_view(), name='usuarios'),
    path('listagemNiveisAcesso/', niveisAcesso.as_view(), name='niveisacesso'),
    path('listagemTelas/', Telas.as_view(), name='telas'),
    path('cadastrarNivel/', views.cadastroNivel, name='cadastronivel'),
    path('cadastrarMenu/', views.cadastroTela, name='cadastromenu'),

    path('AtualizaUsuario/<int:usuario_id>', views.alteraUsuario, name='atualizausuario'),
    path('AtualizaNivel/<int:pk>/', alteraNivel.as_view(), name='atualizanivelacesso'),
]
