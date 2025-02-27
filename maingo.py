from django.db import models
from django.utils import timezone


class Player(models.Model):
    username = models.CharField(max_length=100, unique=True)
    first_login = models.DateTimeField(default=timezone.now)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    def daily_login(self):  # Ежедневный вход
        self.points += 5  # Начисляем баллы
        self.save()
        return f"Points added for player {self.username}. Total points: {self.points}"

    def add_boost(self, boost_type, boost_amout):
        new_boost = Boost(type=boost_type, amout=boost_amout, player=self)
        new_boost.save()
        return f"Boost {boost_type} added to player {self.username}"


class Boost(models.Model):
    type = models.CharField(max_length=100)
    amount = models.IntegerField()
    player = models.ForeignKey(Player, related_name="boosts", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} bost for {self.player.username}"
