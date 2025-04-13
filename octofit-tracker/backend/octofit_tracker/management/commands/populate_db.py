from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        try:
            user1, created = User.objects.get_or_create(email='john.doe@example.com', defaults={'name': 'John Doe', 'age': 25})
            user2, created = User.objects.get_or_create(email='jane.smith@example.com', defaults={'name': 'Jane Smith', 'age': 30})
        except ObjectDoesNotExist:
            self.stdout.write(self.style.WARNING('Users already exist. Skipping creation.'))

        # Create test teams
        Team.objects.get_or_create(name='Team Alpha', defaults={'members': [user1.email, user2.email]})

        # Create test activities
        Activity.objects.get_or_create(user=user1, activity_type='Running', defaults={'duration': 30})
        Activity.objects.get_or_create(user=user2, activity_type='Cycling', defaults={'duration': 45})

        # Create test leaderboard entries
        Leaderboard.objects.get_or_create(user=user1, defaults={'score': 100})
        Leaderboard.objects.get_or_create(user=user2, defaults={'score': 150})

        # Create test workouts
        Workout.objects.get_or_create(name='Push-ups', defaults={'description': 'Do 20 push-ups'})
        Workout.objects.get_or_create(name='Squats', defaults={'description': 'Do 30 squats'})

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
