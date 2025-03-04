# OrgPulse

OrgPulse is a web application designed to streamline and manage organ donation processes. Built with Python and Django, it provides a platform for individuals to register as organ donors and for administrators to efficiently oversee donor information.

## Features

- **Donor Registration**: Enables individuals to sign up as organ donors, providing necessary personal and medical information.
- **Admin Dashboard**: Allows administrators to securely view, manage, and update donor details.
- **Responsive Design**: Ensures accessibility and usability across various devices, including desktops, tablets, and smartphones.

## Installation

Follow these steps to set up OrgPulse locally:

1. **Clone the Repository**

```bash
git clone https://github.com/JudahJL/orgpulse.git
cd orgpulse
```

2. **Create and Activate a Virtual Environment**

- Create the virtual environment using:

```bash
python -m venv .venv
```

- Then, activate it:

```bash
source .venv/bin/activate # On Windows, use '.venv\Scripts\activate'
```

3. **Install Dependencies**

- Install the required packages with:

```bash
python -m pip install -r requirements.txt
```

4. **Create a `.env` File**

- In the project's root directory, create a file named .env and add the following environment variables:

```ini
DJANGO_DEBUG = True
SECRET_KEY = ''
DJANGO_EMAIL_HOST_USER = ''
DJANGO_EMAIL_HOST_PASSWORD = ''
```

- Open your terminal (make sure your virtual environment is activated)

- Paste the below code into your shell (use mouse right side button to paste the copied code, `as Ctrl+V may not work`)-

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

```

* Copy the `SECRET_KEY`(whatever you got in the output), and paste it in your `.env` file after `SECRET_KEY=`.

5. **Apply database migrations:**

```bash
python manage.py migrate
```

7. **Start the development server:**

```bash
python manage.py runserver
```

8. **Open your web browser and navigate to:**

```
http://127.0.0.1:8000/
```