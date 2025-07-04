# Vacation Planner

A Django-based web application for planning and managing vacations.

## Features

- User registration and authentication
- View available vacations
- Like/unlike vacations (for regular users)
- Add, edit, and delete vacations (for admin users)
- Responsive design with Bootstrap
- REST API endpoints

## Technology Stack

- Backend: Django 5.0
- Database: PostgreSQL
- Frontend: HTML, CSS (Bootstrap 5), JavaScript
- Authentication: Django-allauth
- API: Django REST Framework

## Prerequisites

- Python 3.8 or higher
- PostgreSQL
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AlexeyKoz/django_vacation_project_jb.git
cd vacation-planner
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the following variables:
```
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=project_db
DB_USER=postgres
DB_PASSWORD=1234
DB_HOST=localhost
DB_PORT=5432
```

5. Create the database:
```bash
createdb project_db
```

6. Create migrations:
```bash
python manage.py makemigrations
```


7. Run migrations:
```bash
python manage.py migrate
```

8. Create necessary directories:
```bash
mkdir static media
```

9. Populate the database with initial data:
```bash
python manage.py populate_db
```

## Running the Application

1. Start the development server:
```bash
python manage.py runserver
```

2. Visit http://127.0.0.1:8000/ in your browser

## Running Tests

```bash
python manage.py test
```
