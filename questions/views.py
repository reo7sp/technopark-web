from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from questions.models import sample_questions, sample_tags, sample_comments, sample_user, sample_users


def _paginate(objects_list, request):
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


def _sidebar_context():
    return {
        'current_user': sample_user(),
        'popular_tags': sample_tags()[:5],
        'best_members': sample_users()[:5],
    }


@require_GET
def index(request):
    context = {
        'questions': _paginate(sample_questions(), request),
    }
    context.update(_sidebar_context())
    return render(request, 'index.html', context)


@require_GET
def hot(request):
    context = {
        'questions': _paginate(sample_questions(), request),
    }
    context.update(_sidebar_context())
    return render(request, 'hot.html', context)


@require_GET
def tag(request, pk):
    context = {
        'tag': sample_tags()[0],
        'questions': _paginate(sample_questions(), request),
    }
    context.update(_sidebar_context())
    return render(request, 'tag.html', context)


def question(request, pk):
    if request.method == 'GET':
        context = {
            'question': sample_questions()[0],
            'comments': _paginate(sample_comments(), request),
        }
        context.update(_sidebar_context())
        return render(request, 'question.html', context)
    elif request.method == 'POST':
        raise NotImplementedError  # TODO


@require_POST
def logout(request):
    raise NotImplementedError  # TODO


def login(request):
    if request.method == 'GET':
        context = {
        }
        context.update(_sidebar_context())
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        raise NotImplementedError  # TODO


def signup(request):
    if request.method == 'GET':
        context = {
        }
        context.update(_sidebar_context())
        return render(request, 'signup.html', context)
    elif request.method == 'POST':
        raise NotImplementedError  # TODO


def ask(request):
    if request.method == 'GET':
        context = {
        }
        context.update(_sidebar_context())
        return render(request, 'ask.html', context)
    elif request.method == 'POST':
        raise NotImplementedError  # TODO


def settings(request):
    if request.method == 'GET':
        context = {
        }
        context.update(_sidebar_context())
        return render(request, 'settings.html', context)
    elif request.method == 'POST':
        raise NotImplementedError  # TODO
