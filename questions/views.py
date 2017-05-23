from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.template.defaulttags import url
from django.views.decorators.http import require_GET, require_POST

from questions.forms import LoginForm, SignupForm
from questions.models import Profile, Tag, Question, Comment


def _paginate(objects_list, request):
    objects_page = []

    paginator = Paginator(objects_list, 10)
    page = request.GET.get('page')
    try:
        objects_page = paginator.page(page)
    except PageNotAnInteger:
        objects_page = paginator.page(1)
    except EmptyPage:
        page = int(page)
        if page < 1:
            objects_page = paginator.page(1)
        elif page > paginator.num_pages:
            objects_page = paginator.page(paginator.num_pages)

    return objects_page


def _sidebar_context(request):
    if request.user is None or request.user.id is None:
        profile = None
    else:
        profile = Profile.objects.get(user_id=request.user.id)
    print(profile)
    return {
        'current_user': profile,
        'popular_tags': Tag.objects.most_popular(5),
        'best_members': Profile.objects.best_members(5),
    }


@require_GET
@login_required
def index(request):
    context = {
        'questions': _paginate(Question.objects.all_new(), request),
    }
    context.update(_sidebar_context(request))
    return render(request, 'index.html', context)


@require_GET
@login_required
def hot(request):
    context = {
        'questions': _paginate(Question.objects.all_hot(), request),
    }
    context.update(_sidebar_context(request))
    return render(request, 'hot.html', context)


@require_GET
@login_required
def tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    context = {
        'tag': tag,
        'questions': _paginate(Question.objects.filter(tag=tag), request),
    }
    context.update(_sidebar_context(request))
    return render(request, 'tag.html', context)


@login_required
def question(request, pk):
    if request.method == 'GET':
        question = Question.objects.get(pk=pk)
        context = {
            'question': question,
            'comments': _paginate(Comment.objects.filter(question=question), request),
        }
        context.update(_sidebar_context(request))
        return render(request, 'question.html', context)
    elif request.method == 'POST':
        raise NotImplementedError  # TODO


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Wrong user or password')

    context = {
        'form': form
    }
    context.update(_sidebar_context(request))
    return render(request, 'login.html', context)


def signup(request):
    if request.method == 'GET':
        form = SignupForm()
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.create(form.cleaned_data['login'], form.cleaned_data['email'], form.cleaned_data['password'],
                                             nickname=form.cleaned_data['nickname'], avatar=form.cleaned_data['avatar'])
            login(request, profile.user)
            return redirect('index')

    context = {
        'form': form
    }
    context.update(_sidebar_context(request))
    return render(request, 'signup.html', context)


@login_required
def ask(request):
    if request.method == 'GET':
        context = {
        }
        context.update(_sidebar_context(request))
        return render(request, 'ask.html', context)
    elif request.method == 'POST':
        raise NotImplementedError  # TODO


@login_required
def settings(request):
    if request.method == 'GET':
        context = {
        }
        context.update(_sidebar_context(request))
        return render(request, 'settings.html', context)
    elif request.method == 'POST':
        raise NotImplementedError  # TODO
