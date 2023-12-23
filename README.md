# Django Emailer Web App

## Overview

This Django-based web application serves as a simple emailer that allows users to send emails using their Gmail credentials. The application also stores sent emails and displays them on the main page. The primary motivation behind creating this project was to explore and test the implementation of SMTP functionality in Django.

## Features

- **Send Emails:** Utilize your Gmail credentials to send emails directly from the web application.
- **Email Logging:** View a list of sent emails on the main page for easy tracking and reference.

## Getting Started

Follow these steps to set up and run the Emailer web app locally:

### Prerequisites

- Python 3.11
- Django 4.2

### Installation

1. Clone the repository:

   ```zsh
   git clone https://github.com/ab-dauletkhan/emailer.git
   # or
   gh repo clone ab-dauletkhan/emailer
   ```

 
1. Navigate to the project directory:

```zsh
cd emailer
``` 
2. Install dependencies:

```zsh
pip install -r requirements.txt
```
### Configuration 
1. Set up your Gmail credentials in the `settings.py` file:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your@gmail.com'
EMAIL_HOST_PASSWORD = 'your-generated-gmail-password'
```
To get EMAIL_HOST_PASSWORD: 
1. Visit https://myaccount.google.com/security
2. Click on 2-Step Verification (you have to enable 2FA)
3. Enter your Google account password
4. At the bottom of the page there is a ***App Passwords***
5. Write any app name, then copy your password and paste it to ***EMAIL_HOST_PASSWORD***

### Run the Application 
1. Apply migrations:

```zsh
python manage.py makemigrations
python manage.py migrate
``` 
2. Start the development server:

```zsh
python manage.py runserver
``` 
3. Open your browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  to access the Emailer.
## Usage
1. Navigate to the web app and use the provided interface to send emails.
2. Check the main page to view the list of sent emails.


## Disclaimer

This web application is created solely for learning and testing purposes. Feel free to use, modify, and extend it as you explore Django and SMTP functionality. This project is not intended for production use and may not adhere to security best practices.
