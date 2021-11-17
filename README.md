# DjangoReactBackend
The backend app of my Django React test App

# Dependencies
- Python 3.8
- Pip
  - ```python -m pip install --upgrade pip```
- Pipenv
  - ```pip install pipenv```

# Running
- In first run:
  - ```pipenv install```
  - ```pipenv shell```
  - ```python manage.py migrate```
  
- After:
  - ```pipenv shell```
  - ```python manage.py runserver```

- Debug using VSCode:
  - run pipenv install command
  - select default interpreter as the backend virtual env
  - run one of two commands with VSCode debug panel
