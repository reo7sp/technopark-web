from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

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


def _sidebar_context():
    return {
        'current_user': Profile.objects.get(user__username='admin'),
        'popular_tags': Tag.objects.most_popular(5),
        'best_members': Profile.objects.best_members(5),
    }


@require_GET
def index(request):
    context = {
        'questions': _paginate(Question.objects.all_new(), request),
    }
    context.update(_sidebar_context())
    return render(request, 'index.html', context)


@require_GET
def hot(request):
    context = {
        'questions': _paginate(Question.objects.all_hot(), request),
    }
    context.update(_sidebar_context())
    return render(request, 'hot.html', context)


@require_GET
def tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    context = {
        'tag': tag,
        'questions': _paginate(Question.objects.filter(tag=tag), request),
    }
    context.update(_sidebar_context())
    return render(request, 'tag.html', context)


def question(request, pk):
    if request.method == 'GET':
        question = Question.objects.get(pk=pk)
        context = {
            'question': question,
            'comments': _paginate(Comment.objects.filter(question=question), request),
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
