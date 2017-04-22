from django.db import models


class Question:
    pass


class Comment:
    pass


class Tag:
    pass


class User:
    pass


def sample_tags():
    tags = []
    for i in range(1, 15):
        tag = Tag()
        tag.name = 'tag ' + str(i)
        tag.slug = tag.name.replace(' ', '-')
        tags.append(tag)
    return tags


def sample_comments():
    comments = []
    for i in range(1, 45):
        comment = Comment()
        comment.id = 1
        comment.text = 'comment ' + str(i)
        comment.rating = 228
        comment.is_correct = i % 2 == 0
        comment.image_url = '/static/images/profile.png'
        comments.append(comment)
    return comments


def sample_questions():
    questions = []
    for i in range(1, 60):
        question = Question()
        question.id = i
        question.title = 'title ' + str(i)
        question.text = 'text' + str(i)
        question.rating = 228
        question.tags = sample_tags()[:3]
        question.comments_count = 2
        question.image_url = '/static/images/profile.png'
        questions.append(question)
    return questions


def sample_users():
    users = []
    for i in range(1, 15):
        user = User()
        user.login = 'login ' + str(i)
        user.email = 'a@a.com'
        user.nickname = 'nickname ' + str(i)
        users.append(user)
    return users


def sample_user():
    user = User()
    user.login = 'login'
    user.email = 'a@a.com'
    user.nickname = 'nickname'
    return user
