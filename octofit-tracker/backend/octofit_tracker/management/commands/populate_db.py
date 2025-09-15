from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

# Define models for test data
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    user_email = models.EmailField()
    workout_name = models.CharField(max_length=100)
    reps = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user_email = models.EmailField()
    score = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear collections
        Team.objects.all().delete()
        User.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team='Marvel'),
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel'),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC'),
            User(name='Batman', email='batman@dc.com', team='DC'),
        ]
        for user in users:
            user.save()

        # Activities
        activities = [
            Activity(user_email='spiderman@marvel.com', activity_type='Running', duration=30),
            Activity(user_email='ironman@marvel.com', activity_type='Cycling', duration=45),
            Activity(user_email='wonderwoman@dc.com', activity_type='Swimming', duration=60),
            Activity(user_email='batman@dc.com', activity_type='Yoga', duration=20),
        ]
        for activity in activities:
            activity.save()

        # Workouts
        workouts = [
            Workout(user_email='spiderman@marvel.com', workout_name='Push Ups', reps=50),
            Workout(user_email='ironman@marvel.com', workout_name='Pull Ups', reps=30),
            Workout(user_email='wonderwoman@dc.com', workout_name='Squats', reps=40),
            Workout(user_email='batman@dc.com', workout_name='Lunges', reps=35),
        ]
        for workout in workouts:
            workout.save()

        # Leaderboard
        leaderboard = [
            Leaderboard(user_email='spiderman@marvel.com', score=100),
            Leaderboard(user_email='ironman@marvel.com', score=90),
            Leaderboard(user_email='wonderwoman@dc.com', score=95),
            Leaderboard(user_email='batman@dc.com', score=85),
        ]
        for entry in leaderboard:
            entry.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
