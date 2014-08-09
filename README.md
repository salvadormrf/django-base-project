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
	│       ├── admin.py
	│       ├── __init__.py
	│       ├── models.py
	│       ├── tests.py
	│       └── views.py
	├── libs
	│   └── testlib
	│       ├── __init__.py
	│       └── utils.py
	├── manage.py
	├── project_name
	│   ├── __init__.py
	│   ├── settings
	│   │   ├── base.py
	│   │   ├── dev.py
	│   │   ├── __init__.py
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

