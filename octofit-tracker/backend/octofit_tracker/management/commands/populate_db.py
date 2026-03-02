from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Create users
        users = [
            User(name='Tony Stark', email='tony@marvel.com', team='marvel', is_superhero=True),
            User(name='Steve Rogers', email='steve@marvel.com', team='marvel', is_superhero=True),
            User(name='Bruce Wayne', email='bruce@dc.com', team='dc', is_superhero=True),
            User(name='Clark Kent', email='clark@dc.com', team='dc', is_superhero=True),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], activity_type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], activity_type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], activity_type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], activity_type='Yoga', duration=20, date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Upper body strength', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Core strength', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
