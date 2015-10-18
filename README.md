# walmart_hackathon
Walmart Hackathon

# To run django-app
```
sudo apt-get install python-pip
sudo pip install django
sudo apt-get install mysql-server
sudo apt-get install build-essential python-dev libmysqlclient-dev
sudo apt-get install python-mysqldb
cp django_app/django_app/settings.py.example django_app/django_app/settings.py
```
  Change the database parameters in the settings.py file.
```
cd django_app
python manage.py migrate
```
  Now to generate the data, go to the data_gen
```
cp settings.ini.example settings.ini #Edit the settings.ini or you can run dump.sql
python manage.py
```
  To run the server
```
python manage.py runserver
```

