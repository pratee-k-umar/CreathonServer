# Interactive Learning Platform - Backend

An interactive learning platform where users can participate in coding and knowledge challenges, with seamless integration between a web interface and a Telegram bot. This backend is built with Django and is responsible for managing core business logic, handling authentication, exposing RESTful APIs, and managing user progress.

## Project Overview

The backend supports:

- **Challenge Management:** Create, update, and manage coding and knowledge challenges with varying difficulties and point values.
- **User Progress Tracking:** Monitor users’ progress through challenges, including status updates and attempt counts.
- **Real-Time Communication:** Integration with WebSocket for live updates to the frontend and Telegram bot.
- **Robust API:** RESTful endpoints for all major functionalities.
- **Security:** User authentication and authorization to protect data and interactions.
- **Quality Assurance:** Unit tests for critical components and detailed API documentation.

## Technologies Used

- **Framework:** Django
- **Database:** PostgreSQL
- **API:** Django
- **Real-Time Updates:** WebSocket
- **Authentication:** Django’s built-in authentication system

## Project Structure

```
├── challenges
│   ├── models.py        # Contains the Challenge model with fields for title, description, difficulty, points, etc.
│   └── ...
├── progress
│   ├── models.py        # Contains the UserProgress model for tracking user challenge statuses
│   └── ...
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

### Challenge Management

Defined in `challenges/models.py`:

```python
class Challenge(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(
        max_length=20,
        choices=[('beginner', 'Beginner'),
                 ('intermediate', 'Intermediate'),
                 ('advanced', 'Advanced')]
    )
    points = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def validate_submission(self, submission):
        # Challenge-specific validation logic
        pass
```

### User Progress Tracking

Defined in `progress/models.py`:

```python
class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[('started', 'Started'),
                 ('submitted', 'Submitted'),
                 ('completed', 'Completed')]
    )
    attempts = models.IntegerField(default=0)
    completed_at = models.DateTimeField(null=True)
```

## Database Schema (PostgreSQL)

The project uses PostgreSQL to manage core data, including:

- **Users and Authentication:** Stores user credentials and profile details.
- **Challenges and Categories:** Maintains the list of challenges, their descriptions, difficulty levels, points, and associated categories.
- **User Progress and Submissions:** Tracks individual user progress, challenge attempts, and completion timestamps.
- **Achievements and Rewards:** (Planned) To incentivize and recognize user progress.

## Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/pratee-k-umar/CreathonServer.git
   cd core
   ```

2. **Set up a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix/MacOS
   # or
   venv\Scripts\activate  # Windows
   ```

3. **Migrate to core:**

   ```bash
   cd core
   ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure the Database:**

   - Ensure PostgreSQL is installed and running.
   - Create a PostgreSQL database.
   - Update the `DATABASES` setting in your `settings.py` with your database credentials.

6. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

7. **Create a Superuser (optional):**

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

## API Endpoints

The backend exposes several RESTful API endpoints. A few examples include:

- **Challenge Management:**
  - `GET /api/challenges/` — List all challenges.
  - `POST /api/challenges/` — Create a new challenge.
  - `GET /api/challenges/<id>/` — Retrieve details for a specific challenge.
  - `PUT/PATCH /api/challenges/<id>/` — Update an existing challenge.
  - `DELETE /api/challenges/<id>/` — Remove a challenge.

- **User Progress:**
  - `GET /api/progress/` — Retrieve the authenticated user's progress.
  - `POST /api/progress/` — Update or create a progress record.

*Note:* For detailed API documentation, refer to the generated API docs (using Django REST Framework's browsable API or an integrated tool like Swagger).

## Testing

To run the unit tests and ensure that all core functionalities work as expected:

```bash
python manage.py test
```

## Future Enhancements

- **Achievements and Rewards:** Adding a system to recognize and reward user progress.
- **Enhanced Real-Time Features:** Improving WebSocket integration for more dynamic user interactions.
- **Robust Logging and Monitoring:** Further strengthening error handling and monitoring capabilities.
- **Expanded API Functionality:** Additional endpoints and features to support new learning activities.

## Contributing

Contributions are welcome! Please fork the repository, create a new branch for your feature or fix, and submit a pull request. Ensure that your code follows the project guidelines and includes relevant tests.