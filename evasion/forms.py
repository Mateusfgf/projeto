from django import forms

from .models import Aluno, Inscricao

class AlunoForm(forms.Form):

	class Meta:
		Nome = forms.CharField(max_length=200)
		Idade = forms.IntegerField()
		Curso = forms.CharField(widget=forms.Textarea)
		Tem_curso_tecnico = forms.BooleanField()
		Tem_curso_superior = forms.BooleanField()
		Ja_desistiu_algum_curso = forms.BooleanField()
		Tem_curso_tecnico = forms.BooleanField()




class InscricaoForm(forms.Form):

	class Meta:

		model = Inscricao





# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         fields = ('author', 'text',)


# class ContatoForm(forms.Form):
#     Remetente = forms.EmailField(required=True)
#     Titulo = forms.CharField(required=True)
#     Texto = forms.CharField(widget=forms.Textarea)