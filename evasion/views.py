from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound, HttpResponse, JsonResponse

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



# def events(request):

# 	{
#   "events": [
#     { "id": 1, "name": "Campus Party", 
#       "description": "Com nove anos de eventos, a Campus Party reúne mais de 8.000 participantes, sendo considerado o maior evento de tecnologia do mundo.", 
#       "contactInfo": "Em caso de dúvidas, entre em contato com informatica@ifsc.edu.br" },
#     { "id": 2, "name": "PICNIC Brasil", "description": "Festival de inovação, tecnologia e criatividade, criado em 2006 em Amsterdam, que teve a sua primeira edição internacional em 2016 no Brasil",
#       "contactInfo": "Em caso de dúvidas, entre em contato com informatica@ifsc.edu.br" },

#     { "id": 3, "name": "Canal do Boi", "description": "Empresas de atuação no agronegócio já reservaram espaço no local da feira. A programação inclui leilões, palestras, shopping de animais, e exposição de máquinas e implementos agropecuários, nos segmentos de nutrição animal, veículos leves e pesados e produtos veterinários.",
#       "contactInfo": "Em caso de dúvidas, entre em contato com alimentos@ifsc.edu.br" }
#   ],
#   "talks": [
#     { "id": 1, "name": "HACKATHON", "eventId": 1, "day":"05/10", "speaker": "Programadores, designers, profissionais da comunicação, de desenvolvimento de software", "time": "19h00" },
#     { "id": 2, "name": "Alimentos 2", "eventId": 1, "day":"05/10",  "speaker": "Palestrante 2 Alimentos", "time": "20h30" },
#     { "id": 3, "name": "Informática 1", "eventId": 1, "day":"06/10",  "speaker": "Palestrante 1 Informática", "time": "08h00" },
#     { "id": 4, "name": "Informática 2", "eventId": 1, "day":"06/10",  "speaker": "Palestrante 2 Informática", "time": "09h30" },
#     { "id": 5, "name": "Informática 3", "eventId": 1, "day":"07/10",  "speaker": "Palestrante 3 Informática", "time": "10h00" },
#     { "id": 6, "name": "Informática 4", "eventId": 2, "day":"07/10",  "speaker": "Palestrante 4 Informática", "time": "11h30" },
#     { "id": 7, "name": "Informática 5", "eventId": 2, "day":"06/10",  "speaker": "Palestrante 5 Informática", "time": "12h00" },
#     { "id": 8, "name": "Informática 6", "eventId": 2, "day":"06/10",  "speaker": "Palestrante 6 Informática", "time": "13h30" },
#     { "id": 9, "name": "Informática 7", "eventId": 2, "day":"07/10",  "speaker": "Palestrante 7 Informática", "time": "14h00" },
#     { "id": 10, "name": "Informática 8", "eventId": 2, "day":"07/10",  "speaker": "Palestrante 8 Informática", "time": "15h30" },
#     { "id": 11, "name": "Informática 9", "eventId": 3, "day":"07/10",  "speaker": "Palestrante 9 Informática", "time": "16h30" },
#     { "id": 12, "name": "Informática 10", "eventId": 3, "day":"06/10",  "speaker": "Palestrante 10 Informática", "time": "17h00" },
#     { "id": 13, "name": "Informática 11", "eventId": 3, "day":"06/10",  "speaker": "Palestrante 11 Informática", "time": "18h30" },
#     { "id": 14, "name": "Informática 12", "eventId": 3, "day":"07/10",  "speaker": "Palestrante 12 Informática", "time": "19h00" }
#   ]
# }

def events(request):
    try:
        post_json = {
            'status': 1,
            'id': 1,
            'description': "Com nove anos de eventos, a Campus Party reúne mais de 8.000 participantes, sendo considerado o maior evento de tecnologia do mundo.",
            'contactInfo': "Em caso de dúvidas, entre em contato com informatica@ifsc.edu.br",
        }
    except ObjectDoesNotExist:
        post_json = {'status': 0}
    return JsonResponse(post_json)

def talks(request):
    try:
        post_json = {
            'status': 1,
            'name': "HACKATHON",
            'eventId': 1,
            'day': "05/10",
            'speaker': "Programadores, designers, profissionais da comunicacao",
            'time': "20h30",            
        }
    except ObjectDoesNotExist:
        post_json = {'status': 0}
    return JsonResponse(post_json)




 # class json(View):
 # 	def get(self, request, nome):
 # 		vagabundo = self.hamming(nome, 'wesley')
 # 		anjo = 100 - vagabundo

 # 		if nome.upper() != 'wesley'.upper():
 # 			anjo, vagabundo = vagabundo, anjo

 # 		data = {
 # 			'nome': nome,
 # 			'anjo': anjo,
 # 			'vagabundo': vagabundo


 # 		}
 # 		return JsonRespnse(data)



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