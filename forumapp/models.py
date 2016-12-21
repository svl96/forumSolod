from django.db import models
# Create your models here.


class Sections(models.Model):
    class Meta:
        db_table = "sections"
    sections_title = models.CharField(max_length=200)
    sections_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.sections_title


class Themes(models.Model):
    class Meta:
        db_table = 'Themes'
    theme_author = models.ForeignKey('auth.User')
    theme_section = models.ForeignKey(Sections)
    theme_title = models.CharField(max_length=200)
    theme_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.theme_title


class Comments(models.Model):
    class Meta:
        db_table = 'Comments'
    comment_author = models.ForeignKey('auth.User')
    comment_theme = models.ForeignKey(Themes)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True, blank=True)
