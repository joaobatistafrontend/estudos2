from sys import setdlopenflags
from tabnanny import verbose
from django.db import models
from stdimage.models import StdImageField
class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobíle'),
        ('ldjango.dbni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=19,choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico

class Cargo(Base):
    cargo = models .CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to='equipe', variations={'thumb':{'width':480, 'height':480}})
    facebook = models.CharField('Facebook', max_length=100,default='#')
    twitter = models.CharField('Twitter'  , max_length=100,default='#')
    instagram = models.CharField('Instagram', max_length=100,default='#')
    
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome

class Features(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Design'),
        ('lni-laptop-phone', 'Notbook'),
        ('ldjango.dbni-rocket', 'Foguete'),
    )
    servico = models.CharField('Servicos', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone',max_length=19, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Features'
        verbose_name_plural = 'Features'

    def __str__(self) :
        return self.servico

class Sobre(Base):
    estatistica = models.CharField('Estatísticas', max_length=100)
    infromacao = models.TextField('Informações', max_length=250)

    class Meta:
        verbose_name = 'Sobre'
    
    def __str__(self):
        return self.estatistica

