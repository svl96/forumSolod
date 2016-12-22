from django.forms import ModelForm
from .models import Comments, Themes, Sections


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_text']


class ThemesForm(ModelForm):
    class Meta:
        model = Themes
        fields = ['theme_title']


class SectionForm(ModelForm):
    class Meta:
        model = Sections
        fields = ['sections_title']

