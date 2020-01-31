# Stock management system
#### A user friendly system that consolidates and secures data on a company and its operations . 13/01/2020
#### Built by :
* [Titus Ouko - scrum master](https://github.com/costamay)
* [Albert Byrone](https://github.com/Albert-Byrone)
* [Tyra Hans](https://github.com/Tyra-hans)
* [Laurent Juma](https://github.com/Laurent-c4)
* [John Karanja](https://github.com/John-5014)
## Nature
The system is built using django.

## Setup
* Create a directory and set up a virtual environment
* Clone this repo to your desktop
* Create a database locally using psql.
* Open your text editor
* Change the database credentials in Afrique/          settings.py to match your local database
* run 'pip install -r' to install all the app requrements

## Bugs
No known bugs. if any, please report to any of the team members above.

## Behavior driven devlopment (BDD)
#### Admin

| Element           | Action               | Behaviour                              |
| ------------------|:--------------------:| --------------------------------------:|
| nav bar           |click                 |navigates to respective url             |
| search            |key in                |retrives materials/ products            |
| filter            |select dates          |retrieves date specific data            |
| log in            |key in credentials    |Allows user access                      |
| admin dashboard   |create users          |users can login                         |
| admin dashboard   |create user groups    |allows users group-specific permissions |
| side nav          |select                |CRUD and filter operations              |
| log out           |click                 |logs out the active user                |              

#### Store keeper

| Element           | Action               | Behaviour                              |
| ------------------|:--------------------:| --------------------------------------:|
| nav bar           |click                 |navigates to respective url             |
| search            |key in                |retrives materials/ products            |
| filter            |select dates          |retrieves date specific data            |
| log in            |key in credentials    |Allows user access                      |
| side nav          |select                |CRUD and filter operations              |
| log out           |click                 |logs out the active user                |  


#### accountant

| Element           | Action               | Behaviour                              |
| ------------------|:--------------------:| --------------------------------------:|
| nav bar           |click                 |navigates to respective url             |
| search            |key in                |retrives materials/ products            |
| filter            |select dates          |retrieves date specific data            |
| log in            |key in credentials    |Allows user access                      |
| side nav          |select                |View and filter operations              |
| log out           |click                 |logs out the active user                |              

## Technologies
* Django
* Python3.6
* Javascript
* Bootstrap4
* PostgreSQL
* HTML
* CSS

## Support and contact details
For feedback , complaints or queries :
 email: tyrahans17@gmail.com

### License
This project is licensed under the terms of the MIT license.