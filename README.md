# ProdCheck

A web app to help people know what products are available in the store before going there. This app can be hosted and implemented independently.

## Getting Started

### Prerequisites

Clone this repo using - 

```
git clone https://github.com/subhamX/ProdCheck.git
```
### Installing

This app is made with Django which needs python3. Once you have python, Install Django -
```
pip install django
```
Then, install all the dependencies using - 

```
pip install -r requirements.txt
```

### Starting the server

Before starting the server you need to migrate the models to the database.
```
python manage.py makemigrations
python manage.py migrate
```
Now to start the server -
```
python manage.py runserver
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
