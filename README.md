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
`python manage.py runserver'
Server can be access at http://127.0.0.1:8000/
