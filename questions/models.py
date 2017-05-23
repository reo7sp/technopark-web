from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


class ProfileManager(models.Manager):
    def create(self, username, email, password, nickname, avatar):
        user = User.objects.create_user(username, email, password)
        return super().create(user=user, avatar=avatar, nickname=nickname)

    def best_members(self, n):
        return self.all()[:n]  # TODO: use likes


class Profile(models.Model):
    objects = ProfileManager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    avatar = models.ImageField()

    @property
    def login(self):
        return self.user.username

    @property
    def email(self):
        return self.user.email

    @property
    def password(self):
        return self.user.password

    @property
    def image_url(self):
        return '/static/images/profile.png'  # TODO


class QuestionManager(models.Manager):
    def all_new(self):
        return self.all()

    def all_hot(self):
        return self.all()  # TODO: rating


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    @property
    def rating(self):
        return self.like_set.filter(is_up=True).count() - self.like_set.filter(is_up=False).count()

    @property
    def image_url(self):
        return '/static/images/profile.png'  # TODO


class Comment(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_correct = models.BooleanField()

    @property
    def rating(self):
        rating = 0
        for like in self.like_set.all():
            rating += 1 if like.is_up else 0
        return rating

    @property
    def image_url(self):
        return '/static/images/profile.png'  # TODO


class TagManager(models.Manager):
    def most_popular(self, n):
        return self.order_by('-questions')[:n]


class Tag(models.Model):
    objects = TagManager()
    slug = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    questions = models.ManyToManyField(Question)

    @property
    def popularity(self):
        return self.questions.count()


class Like(models.Model):
    is_up = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def clean(self):
        if (self.question is not None) and (self.comment is not None):
            raise ValidationError(_('Question and comment cannot be set both'))
