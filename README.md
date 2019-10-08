# ProdCheck

A web app to help people know what products are available in the store before going there. This app can be hosted and implemented independently.

## For Developers
[![Gitter](https://badges.gitter.im/convocation/ProdCheck.svg)](https://gitter.im/convocation/ProdCheck?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
1. First of all fork this repo.
2. Clone the repo - 
```
git clone https://github.com/YOUR_USERNAME/ProdCheck.git
```
3. Installing
This app is made with Django which needs python3. Once you have python
Install all the dependencies using - 
```
pip install -r requirements.txt
```
4. Make the necessary changes. And then commit it.
5. Push it to the server and submit a PR.
6. In case of any help you can always join Gitter.

In case you love contributing don't forget to give a star.

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