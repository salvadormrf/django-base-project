django-base-project
===================

Django template with multiple environments **[local, dev, test, stage, prod]**



#### Install base environment
    # create project virtual environment and install django
    mkvirtualenv myproject
    pip install django
    
    
### Start a new project
    django-admin.py startproject --template=https://github.com/salvadormrf/django-base-project.git myproject




#### Files tree
    .
    ├── apps
    │   └── testapp
    │       ├── __init__.py
    │       ├── admin.py
    │       ├── models.py
    │       ├── tests.py
    │       └── views.py
    ├── libs
    ├── manage.py
    ├── project_name
    │   ├── __init__.py
    │   ├── settings
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── dev.py
    │   │   ├── local.py
    │   │   ├── prod.py
    │   │   ├── stage.py
    │   │   └── test.py
    │   ├── urls.py
    │   └── wsgi.py
    └── requirements
        ├── base.txt
        ├── dev.txt
        ├── local.txt
        ├── prod.txt
        ├── stage.txt
        └── test.txt

