from django import forms

from .models import Aluno, 

class AlunoForm(forms.Form):

    class Meta:
		Nome = forms.CharField(max_length=200)
	    Idade = forms.IntegerField(default=0)
	    Curso = forms.CharField(widget=forms.Textarea)
	    Tem_curso_tecnico = models.BooleanField(default=False)
	    Tem_curso_superior = models.BooleanField(default=False)
	    Ja_desistiu_algum_curso = models.BooleanField(default=False)
	    Tem_curso_tecnico = models.BooleanField(default=False)



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class ContatoForm(forms.Form):
    Remetente = forms.EmailField(required=True)
    Titulo = forms.CharField(required=True)
    Texto = forms.CharField(widget=forms.Textarea)
