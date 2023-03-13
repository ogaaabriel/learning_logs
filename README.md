# Learning Logs

Django app to help track learning.  
Create a list of topics you are studying, take notes and share it with other users.

## Screenshots

### Home page
![Home](./docs/screenshots/home.png)

### Topics page
![Topics](./docs/screenshots/topics.png)

### Topic page
![Topic](./docs/screenshots/topic.png)

## Goals

App developed in order to put into practice my studies on Django.  
Some of the concepts I was able to put into practice:

- Function based views
- ORM
- Forms
- Templates
- Basic auth
- Integration with third party lib

## Tools

[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

## Run locally

The first thing to do is to clone the repository:

```sh
git clone https://github.com/ogaaabriel/learning_logs.git
cd learning_logs
```

Create a virtual environment to install dependencies in and activate it:

```sh
python -m venv venv
source venv/Scripts/activate
```

Then install the dependencies:

```sh
pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:

```sh
python manage.py migrate
python manage.py runserver
```

And navigate to `http://localhost:8000`.
