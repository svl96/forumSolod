from django.shortcuts import render, redirect

# Create your views here.
from .models import Sections, Comments, Themes
from .forms import CommentForm, ThemesForm, SectionForm
from django.contrib import auth


def sections(request):
    args = dict()
    args['sections'] = Sections.objects.all()
    args['username'] = request.user.username
    args['user'] = request.user
    args['isNormalUser'] = request.user.groups.filter(name='normalUser').exists()
    return render(request, 'forumapp/sections.html', args)


def add_section(request):
    if request.POST and request.user.is_staff():
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/')


def del_section(request, section_id):
    if request.user.is_staff:
        section = Sections.objects.get(id=section_id)
        section.delete()
    return redirect('/')


def themes(request, section_id):
    args = dict()
    args['section_id'] = section_id
    args['username'] = request.user.username
    args['themes'] = Themes.objects.filter(theme_section_id=section_id)
    args['isNormalUser'] = request.user.groups.filter(name='normalUser').exists()
    args['form'] = ThemesForm
    return render(request, 'forumapp/themes.html', args)


def comments(request, section_id, theme_id):
    comment_form = CommentForm
    args = dict()
    args['theme_id'] = theme_id
    args['section_id'] = section_id
    args['username'] = request.user.username
    args['user'] = request.user
    args['isNormalUser'] = request.user.groups.filter(name='normalUser').exists()
    args['comments'] = Comments.objects.filter(comment_theme_id=theme_id)
    args['section_title'] = Sections.objects.get(id=section_id).sections_title
    args['form'] = comment_form
    return render(request, 'forumapp/comments.html', args)


def add_theme(request, section_id):
    section = Sections.objects.get(id=section_id)
    if request.POST:
        form = ThemesForm(request.POST)
        if form.is_valid():
            theme = form.save(commit=False)
            theme.theme_author = request.user
            theme.theme_section = section
            form.save()
    return redirect('/{}/themes/'.format(section_id))


def del_theme(request, theme_id):
    theme = Themes.objects.get(id=theme_id)
    section_id = theme.theme_section_id
    if request.user.is_staff or theme.theme_author == request.user:
        theme.delete()
    return redirect('/{}/themes/'.format(section_id))


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


def del_comment(request, comment_id):
    comment = Comments.objects.get(id=comment_id)
    theme = comment.comment_theme
    sections_id = theme.theme_section_id
    if request.user.is_staff or comment.comment_author.username == request.user.username:
        comment.delete()
    return redirect('/{}/themes/{}/'.format(sections_id, theme.id))
