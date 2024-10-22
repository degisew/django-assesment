# Django-Assesment
This project provides a robust authentication system for handling:

OAuth login via social accounts (Google, Facebook, etc.)
Custom email-based registration and authentication
Role-based access control for different user roles (e.g., Admin, Coach, Agent).

## License: MIT

## Settings

Settings are organized for development, and production environment separately under BASE_DIR/config/settings

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy social_auth

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

# Installation
Clone the repository:

git clone https://github.com/degisew/django-assesment.git
cd django-assesment

# Install poetry for dependency management
pipx install poetry
poetry init
poetry shell
poetry install

# Set up environment variables:

Create a .envs/.development and .envs/.production file in the root directory with the following keys:

SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your_google_key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your_google_secret

# Run migrations:

python manage.py migrate

# Run the development server:

python manage.py runserver