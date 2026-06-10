from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return (f"Race name is: {self.name}, "
                f"description is: {self.description}")


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (f"Skill name is: {self.name}, "
                f"bonus is: {self.bonus}")


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Guild name is: {self.name}"


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=False)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (f"Player nickname is: {self.nickname}, "
                f"race is: {self.race}"
                f"guild is: {self.guild if self.guild else 'None'}")
