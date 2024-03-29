# -*- coding: UTF8 -*-
from django.db import models
from registros.model_choices import HORAS, MINUTOS

#class Pontos(models.Model):
#    ponto=models.PositiveSmallIntegerField(u'ponto número')
#    ref=models.CharField(u'referênca',max_length=128,null=True,blank=True)
#    bairro=models.CharField(u'bairro',max_length=26,null=True,blank=True)
#    lograd=models.CharField(u'logradouro',max_length=64,null=True,blank=True)
#    
#    def __unicode__(self):
#        return self.ponto

class Registros(models.Model):
    criado_em=models.DateTimeField('criado em', auto_now_add=True)
    twitter=models.CharField('twitter', max_length=15,default='@morenocunha')#unique
    ponto=models.PositiveSmallIntegerField(u'ponto número',default=5024,help_text='Para encontrar seu ponto acesse <a href=http://rast.vitoria.es.gov.br/pontovitoria/>Ponto Vitória</a>')
    linha=models.PositiveSmallIntegerField(u'linha',default=202)
    horas=models.PositiveSmallIntegerField(u'estou no ponto às',choices=HORAS,default=7)
    minutos=models.PositiveSmallIntegerField(u':',choices=MINUTOS,default=0)
    #hora_trab=models.PositiveSmallIntegerField(u'Também vou sair às',choices=HORAS,default=18,null=True,blank=True)
    #minutos_trab=models.PositiveSmallIntegerField(u':',choices=MINUTOS,default=0,null=True,blank=True)
    
    class Meta:
        #ordering = ["created_at"]
        verbose_name = u"Registro"
        #verbose_name_plural = u"Inscrições"
    
    def __unicode__(self):
        return self.twitter
