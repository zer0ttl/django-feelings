from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
CONDITIONS = (
    (5, 'Joy'),
    (10, 'Passionate'),
    (15, 'Happy'),
    (20, 'Optimistic'),
    (25, 'Content'),
    (30, 'Bored'),
    (31, 'Tired'),
    (33, 'Hungry'),
    (35,'Pessimistic'),
    (40, 'Frustrated'),
    (45,'Overwhelmed'),
    (50,'Dissapointed'),
    (55, 'Worried'),
    (60, 'Angry'),
    (65, 'Jealous'),
    (70, 'Insecure'),
    (75, 'Guilty'),
    (80, 'Fear'),
    (85, 'Grief'),
    (90, 'Despair'),
)


class Thought(models.Model):
    user = models.ForeignKey(User, related_name='thoughts', on_delete=models.CASCADE)
    recorded_at = models.DateField(default=timezone.now, editable=False)
    condition = models.IntegerField(choices=CONDITIONS)
    notes = models.TextField(blank=True, default='')

    def __str__(self):
        return '{}: {}'.format(self.recorded_at.strftime('%Y-%m-%d %H:%M'), self.get_condition_display())

