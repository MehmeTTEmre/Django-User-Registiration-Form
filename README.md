# Django User Registiration Form
In this project, customer registration is done through the admin panel.
## Installation
```
pip install python
pip install django
pip install django-admin-list-filter-dropdown
```

## Usage
Linux & Mac:

```source venv/bin/activate```

Windows:

open command prompt in file directory

```
pip install virtualenv
virtualenv venv
venv\Scripts\activate
python manage.py makemigrations
python manage.py migrate
```
To create an admin account:

```python manage.py createsuperuser```

then you set username and password

Run the server:

```python manage.py runserver```

After the python manage.py runserver command, we paste the local url that appears in the command prompt into the browser.

![1](https://user-images.githubusercontent.com/61835738/156841757-14a81eb6-5372-4ddf-b00a-6363d0901986.png)

After adding the /admin tag to the local url (http://127.0.0.1:8000/admin), we will be directed to the admin panel.

![3](https://user-images.githubusercontent.com/61835738/156841631-fefff38a-ae57-4420-8168-2047b6b2bf07.png)

