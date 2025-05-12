You need to run this on docker and fill the .env, please note that it requires Docker to run and it is postgresql you need also to use email to the .env.
step 1 - python -m venv venv
step 2 - .\venv\Scripts\activate
step 3 - pip install -r requirements.txt
step 4 - python manage.py migrate
step 5 - python manage.py runserver
