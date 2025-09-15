from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.user_email} - {self.activity_type}"

class Workout(models.Model):
    user_email = models.EmailField()
    workout_name = models.CharField(max_length=100)
    reps = models.IntegerField()
    def __str__(self):
        return f"{self.user_email} - {self.workout_name}"

class Leaderboard(models.Model):
    user_email = models.EmailField()
    score = models.IntegerField()
    def __str__(self):
        return f"{self.user_email} - {self.score}"
