from django.contrib.auth.models import User
from django.db import models


class Annotation(models.Model):
    account = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)
    name = models.CharField(max_length=45)
    description = models.TextField()
    deadline = models.DateTimeField()  # format("YYYY-MM-DD\ HH:mn:sc")
    reminder = models.TimeField()  # format("HH:Mn:Sc")
    over = models.BooleanField(default=False)
    
    # viewers
    like = models.ManyToManyField(User, related_name='fan_zone',  blank=True, null=True)
    unlike = models.ManyToManyField(User, related_name='contests', blank=True, null=True)
    
    objects = models.Manager()

    def __str__(self) -> str:
        return f'{self.id}-----{self.name}-------{self.deadline.date()}'

    @staticmethod
    def get_nb_views(self) -> int:
        likers = Liker.objects.filter(action=True)
        dislikers = DisLiker.objects.filter(action=True)
        return len(likers)+len(dislikers)

    @staticmethod
    def get_nb_likes(self) -> int:
        likers = Liker.objects.filter(action=False)
        return len(likers)

    @staticmethod
    def get_nb_unlikes(self) -> int:
        dislikers = DisLiker.objects.filter(action=True)
        return len(dislikers)


class Task(models.Model):
    relation = models.ForeignKey(to=Annotation, on_delete=models.CASCADE)
    action = models.CharField(max_length=75)
    objects = models.Manager()


class Liker(models.Model):
    action = models.BooleanField(default=False)
    one = models.ForeignKey(User, on_delete = models.CASCADE)
    annotation = models.ForeignKey(Annotation, on_delete = models.CASCADE)


class DisLiker(models.Model):
    action = models.BooleanField(default=False)
    one = models.ForeignKey(User, on_delete = models.CASCADE)
    annotation = models.ForeignKey(Annotation, on_delete = models.CASCADE)


"""
    def regulator(self):
        if self.like:
            self.dislike != self.like
        else:
            self.like != self.dislike"""