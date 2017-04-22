import random

from django.contrib.auth.models import User
from django.core.management import BaseCommand

from questions.models import Tag, Profile, Question, Comment, Like

random_words = ['ice-cream', 'cats', 'sky', 'peace', 'yellow', 'five', 'great', 'girls', 'attitude', 'wonderful']


class Command(BaseCommand):
    def handle(self, *args, **options):
        self._populate_tags()
        self._populate_profiles()
        self._populate_questions()
        self._populate_comments()
        self._populate_likes()

    def _populate_profiles(self):
        if User.objects.count() > 0:
            return
        user = User.objects.create_superuser('admin', 'admin@example.com', '1234', first_name='The admin user')
        Profile.objects.create(user=user)

    def _populate_questions(self):
        if Question.objects.count() > 0:
            return
        tags = Tag.objects.all()
        for i in range(25):
            question = Question.objects.create(title=self._get_random_word(), text=self._get_random_text(), author=Profile.objects.first())
            for j in range(3):
                question.tag_set.add(random.choice(tags))

    def _populate_comments(self):
        if Comment.objects.count() > 0:
            return
        for question in Question.objects.all():
            for i in range(random.randint(0, 30)):
                Comment.objects.create(text=self._get_random_text(), is_correct=random.random() < 0.5, question=question,
                                       author=Profile.objects.first())

    def _populate_tags(self):
        if Tag.objects.count() > 0:
            return
        for word in random_words:
            Tag.objects.create(slug=word, name=word)

    def _populate_likes(self):
        if Like.objects.count() > 0:
            return
        for question in Question.objects.all():
            for i in range(random.randint(0, 30)):
                Like.objects.create(is_up=random.random() < 0.7, question=question, author=Profile.objects.first())
        for comment in Comment.objects.all():
            for i in range(random.randint(0, 30)):
                Like.objects.create(is_up=random.random() < 0.7, comment=comment, author=Profile.objects.first())

    def _get_random_word(self):
        return random.choice(random_words)

    def _get_random_text(self):
        text = ''
        for i in range(random.randint(5, 25)):
            text += str(random.random())
            text += ' '
        return text
