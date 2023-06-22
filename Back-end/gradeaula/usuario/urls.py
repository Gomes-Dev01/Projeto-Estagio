from django.urls import path
from  django.contrib.auth import views
from . import views
from .views import UsuariosListView, NiveisAcessoListView, cadastroTela, TelasListView, alteraNivel, alteraMenu



urlpatterns = [
    path('', views.index, name='usuario-login'),
    path('usuario/', views.homeUsuario, name='usuario-home'),
    path('listagemUsuario/', UsuariosListView.as_view(), name='usuarios'),
    path('listagemNiveisAcesso/', NiveisAcessoListView.as_view(), name='niveisacesso'),
    path('listagemTelas/', TelasListView.as_view(), name='telas'),
    path('cadastrarNivel/', views.cadastroNivel, name='cadastronivel'),
    path('cadastrarMenu/', views.cadastroTela, name='cadastromenu'),

    path('AtualizaUsuario/<int:usuario_id>', views.alteraUsuario, name='atualizausuario'),
    path('AtualizaNivel/<int:nivel_id>', views.alteraNivel, name='atualizanivelacesso'),
    path('AtualizaMenu/<int:menu_id>', views.alteraMenu, name='atualizamenu'),
]
