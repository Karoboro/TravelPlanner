# To run the project, please follow these steps

**These instructions are for Windows users only**

## Installing virtual environment and Django
- Create a folder


- Open that folder with VSCode

- In your terminal

`python.exe -m pip install --upgrade pip`

`python -m venv venv`

`.\venv\Scripts\activate`

` python -m pip install Django`


## Clone our project
In the same folder as above: 

`git clone https://github.com/Karoboro/TravelPlanner.git`

`cd TravelPlanner`


## Build the database, create superusers
Navigate To /TravelPlanner

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuperuser`

username: admin

email: blank 

password: admin

`python populate_database.py`



## To run our app
Make sure you finish all steps above

`python manage.py runserver`

Server can be access at http://127.0.0.1:8000/

# Folder Structure

## TravelPlanner
Contains the settings and is the base app for Django.

## main
Contains our module / app, this is where the logic of our website is located.
Also contains our model file, the structure to the sqlite database.
Url file for the resource pathing in our site.
Views file for our logic in routing and rendering pages.
Test file for our unit and function tests.

### templates
Contains our views, a base layout that we perform structure scaffolding on top of.
Along with other views for different pages to the site.

### static
Our static files, such as images (logos and icons) and a stylesheet file.

### fixtures
Our fixture file, data to be seeded into our database to be used for unit and function testing.

# Notes about the Project
Password reset for forgot password currently outputs email message to the django terminal to avoid 
the need to create fake user emails.

Click on the reset password link inside the email body in django terminal to be redirected to 
the password reset page.
