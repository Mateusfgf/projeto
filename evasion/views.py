from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Aluno
# from .forms import AlunoForm, CommentForm, ContatoForm


def listar_dados(request):
	    posts = Aluno.objects.filter(data_resposta__lte=timezone.now()).order_by('data_resposta')
	    return render(request, 'evasion/pagina_inicial.html', {'posts': posts})


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