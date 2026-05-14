from django.db import models
from django.contrib.auth.models import User

class Trenink(models.Model):
    nazev = models.CharField(max_length=100)
    typ = models.CharField(max_length=10)
    delka = models.IntegerField()

    def __str__(self):
        return f"{self.typ} ({self.delka} min)"

class Rezervace(models.Model):
    uzivatel = models.ForeignKey(User, on_delete=models.CASCADE)
    trenink = models.ForeignKey(Trenink, on_delete=models.CASCADE)
    datum = models.DateField()
    cas = models.TimeField()

    def __str__(self):
        return f"{self.uzivatel.username} - {self.trenink.typ} v {self.datum}"
