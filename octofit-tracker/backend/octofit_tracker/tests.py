from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, 'Marvel')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user_email='test@example.com', activity_type='Running', duration=30)
        self.assertEqual(activity.user_email, 'test@example.com')
        self.assertEqual(activity.activity_type, 'Running')
        self.assertEqual(activity.duration, 30)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user_email='test@example.com', workout_name='Push Ups', reps=20)
        self.assertEqual(workout.user_email, 'test@example.com')
        self.assertEqual(workout.workout_name, 'Push Ups')
        self.assertEqual(workout.reps, 20)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(user_email='test@example.com', score=100)
        self.assertEqual(leaderboard.user_email, 'test@example.com')
        self.assertEqual(leaderboard.score, 100)
