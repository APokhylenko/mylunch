# Django Vue project

This is a simple Django - Vue project for collective food order.

 

## Features

- Django 1.11
- Vue 2.5.2
- Django project [template](https://github.com/jpadilla/django-project-template)
- JSON Web Token Authentication [django-rest-framework-jwt](https://github.com/GetBlimp/django-rest-framework-jwt)
- Import from file [django-import-export](https://github.com/django-import-export/django-import-export)

## How to install

To install backend:
```bash
$ create virtual env
$ git clone https://github.com/APokhylenko/mylunch.git
$ cd mylunch/backend
$ pip install -r req.txt
$ mv example.env .env
```
- open .env and add 'SECRET_KEY'
- setup database and add DATABASE_URL to .env
						OR
 or you can use sqlite - just uncomment it in settings
```bash
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
To install frontend:
- open new terminal window
```bash
$ cd ./frontend
$ npm install
$ npm run dev
```
**Note**: take a look at [template](https://github.com/jpadilla/django-project-template) used in this project 

## Usage
- Add first and last names to superuser.
- Upload test data from 'static' folder.
- Add products
- order lunch :) 

## License
MIT

