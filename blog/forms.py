from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.RadioSelect(attrs={"class": "form-check-input"}),
        empty_label=None,
        required=True,
    )

    class Meta:
        model = Post
        fields = ["postTitle", "content", "category"]
        widgets = {
            "postTitle": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].label_from_instance = lambda obj: f"{obj.name}"
