from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy

from evasion.models import Inscricao, Aluno
from evasion.forms import InscricaoForm



def home(request):
        return render(request,'pagina_inicial.html')

class Criar(CreateView):
        template_name = 'evasion/cadastro.html'
        fields = '__all__'
        model = Inscricao
        success_url = reverse_lazy('lista')

class Lista(ListView):
        template_name = 'evasion/lista.html'
        model = Inscricao
        context_object = 'nome'


def listar_dados(request):
	    # posts = Aluno.objects.filter(data_resposta__lte=timezone.now()).order_by('data_resposta')
	    # return render(request, 'evasion/pagina_inicial.html', {'posts': posts})

		return render(request, 'evasion/pagina_inicial.html')

def listar_graficos(request):
	    post = get_object_or_404(Aluno, pk=pk)
	    return render(request, 'evasion/mostrar_grafico.html', {'post': post})


def formulario_usuario(request):
	return render(request, 'evasion/formulario_usuario.html')




	# if form.is_valid():
 #            Nome = usuario_form.cleaned_data['Remetente']
 #            Idade = usuario_form.cleaned_data['Titulo']
 #            Curso = usuario_form.cleaned_data['Texto']


	# 	eviar_resposta(Nome, Idade, Curso)
	# return HttpResponseRedirect('/thanks/')










	# if request.method == 'GET':
	# 	usuario_form = AlunoForm():
 #            Nome = usuario_form.cleaned_data['Remetente']
 #            Idade = usuario_form.cleaned_data['Titulo']
 #            Curso = usuario_form.cleaned_data['Texto']
 #    return render(request, 'evasion/formulario_usuario.html', {'form': usuario_form})


	# request.method == 'GET':
 #    form = AlunoForm()
 #    return render(request, 'evasion/formulario_usuario.html', {'form': form})



		# Nome = forms.CharField(max_length=200)
	 #    Idade = forms.IntegerField(default=0)
	 #    Curso = forms.CharField(widget=forms.Textarea)
	 #    Tem_curso_tecnico = models.BooleanField(default=False)
	 #    Tem_curso_superior = models.BooleanField(default=False)
	 #    Ja_desistiu_algum_curso = models.BooleanField(default=False)
	 #    Tem_curso_tecnico = models.BooleanField(default=False)