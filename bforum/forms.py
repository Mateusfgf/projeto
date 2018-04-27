from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class ContatoForm(forms.Form):
    Remetente = forms.EmailField(required=True)
    Titulo = forms.CharField(required=True)
    Texto = forms.CharField(widget=forms.Textarea)

# class CreateUser(forms.ModelForm)
# 		model = CreateUser
# 		fields = ('author', 'password')