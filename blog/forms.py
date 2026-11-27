from django import forms
from .models import Post


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]
        widgets = {
            "title": forms.TextInput(attrs={'style': 'width: 225px;', 'class': 'form-control'}),

            'body': forms.Textarea(attrs={
                'placeholder': 'Enter your post here...',
                'class': 'form-control',
                'style': 'width: 600px;'}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

