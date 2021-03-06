from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Set(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("sets_detail", kwargs={"pk": self.id})

class Card(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    power = models.IntegerField()
    toughness = models.IntegerField()
    sets = models.ManyToManyField(Set)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'card_id': self.id})


FORMAT = (
    ('MOD','Modern'),
    ('STD','Standard'),
    ('PNR','Pioneer'),
    ('LGC','Legacy'),
    ('VIN','Vintage'),
    ('PAU','Pauper'),
    ('CMD','Commander'),
    ('BRW','Brawl'),
)

class Format(models.Model):
    date = models.DateField('Date Last Played')
    formats = models.CharField(
        max_length=3,
        choices=FORMAT,
        default=FORMAT[0][0]
    )
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_formats_display()} on {self.date}'
    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for card_id: {self.card_id} @{self.url}"