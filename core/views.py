from django.views.generic import FormView
from .models import Servico, Funcionario, Features, Sobre
from .forms import ContatoForm
from django.contrib import messages
from django.urls import reverse_lazy


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context ['servicos'] = Servico.objects.order_by('?').all()
        context ['funcionarios'] = Funcionario.objects.order_by('?').all()
        context ['features'] = Features.objects.order_by('?').all()
        context ['sobre'] = Sobre.objects.all()
        return context

    def form_valid(self, form, *args,**kwargs):

        form = ContatoForm(self.request.POST or None)
        if self.request.method == 'POST':
            if form.is_valid():
                nome = form.cleaned_data['nome']
                email = form.cleaned_data['email']
                assunto = form.cleaned_data['assunto']
                mensagem = form.cleaned_data['mensagem']

                print(f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}')

                messages.success(self.request,'E-mail enviado com sucesso!')
            else:
                messages.error('Falha ao envio do E-mail')

            return super(IndexView, self).form_valid(form,*args, **kwargs)





