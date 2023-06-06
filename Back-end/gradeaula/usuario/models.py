from django.db import models
from django.contrib.auth.models import User


class NivelAcesso(models.Model):
    id = models.AutoField(primary_key=True)
    ds_nivelAcesso = models.CharField(max_length=30)
    
    def __str__(self):
        return self.ds_nivelAcesso


class Usuario(models.Model):
    id_niveis = models.ManyToManyField(NivelAcesso, related_name='usuarios')
    senha = models.CharField(max_length=50)
    nome  = models.CharField(max_length=50)
    status = models.CharField(max_length=1)
    inclusao = models.DateField(auto_now=True)
    usuario = models.CharField(max_length=50)    

   
    def __str__(self):
        return "%s %s %s %s" %(self.nome, self.status, self.usuario, self.id_niveis)




#class UsuarioNivelAcesso(models.Model):
#    id_usuarios = models.ManyToManyField(Usuario)
#    id_nivelAcesso = models.ManyToManyField(nivelAcesso)

    #def __str__(self):
   #    return "{} : {} ".format(self.id_usuario, self.id_nivelAcesso)


class MenuEntrada(models.Model):
    id = models.AutoField(primary_key=True)
    ds_MenuEntrada = models.CharField(max_length=50)
    nivel_MenuEntrada = models.IntegerField(default=0)
    ordem = models.CharField(max_length=50)
    nomePagina = models.CharField(max_length=100)

class NivelEntradaMenu(models.Model):
    nivelAcesso = models.ForeignKey(NivelAcesso, on_delete=models.PROTECT)
    MenuEntrada = models.ForeignKey(MenuEntrada, on_delete=models.PROTECT)
    alteracao = models.BooleanField
    Exclusao = models.BooleanField