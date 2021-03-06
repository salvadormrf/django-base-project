django-base-project
===================

Django template with multiple environments **[local, dev, test, stage, prod]**



#### Install base environment
    # create project virtual environment and install django
    mkvirtualenv myproject
    pip install django
    
    
### Start a new project
    django-admin.py startproject --template=https://github.com/salvadormrf/django-base-project/archive/master.zip myproject


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


#### TODO
- docs
- basic html structure | base, 400, 500
- static assets
- debug mode, enable static dev server
- add debug toolbar
- static version for assets
- get some cool stuff from https://github.com/xenith/django-base-template and https://github.com/twoscoops/django-twoscoops-project

