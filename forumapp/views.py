from django.shortcuts import render, redirect

# Create your views here.
from .models import Sections, Comments, Themes
from .forms import CommentForm
from django.contrib import auth


def sections(request):
    args = dict()
    args['sections'] = Sections.objects.all()
    args['username'] = request.user.username
    return render(request, 'forumapp/sections.html', args)


def themes(request, section_id):
    args = dict()
    args['section_id'] = section_id
    args['username'] = request.user.username
    args['themes'] = Themes.objects.filter(theme_section_id=section_id)
    return render(request, 'forumapp/themes.html', args)


def comments(request, theme_id):
    comment_form = CommentForm
    args = dict()
    args['theme_id'] = theme_id
    args['username'] = request.user.username
    args['comments'] = Comments.objects.filter(comment_theme_id=theme_id)
    args['form'] = comment_form
    return render(request, 'forumapp/comments.html', args)


def add_comment(request, theme_id):
    theme = Themes.objects.get(id=theme_id)
    section = Sections.objects.get(id=theme.theme_section_id)
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.username:
            comment = form.save(commit=False)
            comment.comment_theme = theme
            comment.comment_author = request.user
            form.save()
    return redirect('/{}/themes/{}/'.format(section.id, theme_id))
