# Test data for the OctoFit Tracker application

def get_test_data():
    return {
        "users": [
            {"email": "john.doe@example.com", "name": "John Doe", "age": 25},
            {"email": "jane.smith@example.com", "name": "Jane Smith", "age": 30}
        ],
        "teams": [
            {"name": "Team Alpha", "members": ["john.doe@example.com", "jane.smith@example.com"]}
        ],
        "activities": [
            {"user_email": "john.doe@example.com", "activity_type": "Running", "duration": 30},
            {"user_email": "jane.smith@example.com", "activity_type": "Cycling", "duration": 45}
        ],
        "leaderboard": [
            {"user_email": "john.doe@example.com", "score": 100},
            {"user_email": "jane.smith@example.com", "score": 150}
        ],
        "workouts": [
            {"name": "Push-ups", "description": "Do 20 push-ups"},
            {"name": "Squats", "description": "Do 30 squats"}
        ]
    }
