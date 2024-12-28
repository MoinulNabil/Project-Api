Run
===
You must have reliable/latest version of python installed on your machine to use this application.
I have used 3.12.3.

With that, please follow the instructions below to run the app:

Clone the repo and move into the project root.

```bash

git clone https://github.com/MoinulNabil/Project-Api.git
cd Project-Api

```

Install the dependencies.

I would recommend to work on a virtual environment. I have used virtualenv package to create a virtual environment you may wanna use other package. So install this as well if you already haven't..

Create a virtual environment by the following command.

```bash

virtualenv venv

```

Now activate the virtualenv:

**On Linux***

```bash

source venv/bin/activate

```    
***On Windows***

If you are using git bash

```bash

source venv/Scripts/activate

```
Now install the dependencies, run the migrations and spin up the server:

```bash

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

```


Now go to http://localhost:8000/swagger/ or http://localhost:8000/redoc/

And you will find the api docs/list provided by swagger here.

Usage
===
An api client such as Postman is recomended to test apis using TokenAuthentication.

Api can also be tested through a browser using BasicAuthentication.
First of create a superuser, then login as admin then you can test the apis using BasicAuthentication.