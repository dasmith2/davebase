# davebase

This is my starting point for new Django projects on Heroku

Now, Github doesn't allow you to fork your own repositories so easily. So to
create a new project forked from this project, first create a new EMPTY
repository on Github, so make sure you DON'T check "Initialize this repository
with a README". Then clone your new repository locally and cd into it. Next,
add an upstream remote to this repository like so

    git clone git@github.com:dasmith2/my-new-repo.git
    cd my-new-repo
    git remote add upstream git@github.com:dasmith2/davebase.git
    git pull upstream master  # Any time you want to pull from davebase
    git push  # Any time you want to push to my-new-repo

You'll need to make some changes.

1. Update the name, description, and repository in app.json
1. Create a main/local_settings.py file
1. You can delete the example app entirely

You'll need to set up a database.

    sudo apt-get update
    sudo apt-get install postgresql postgresql-contrib
    # OK, I admit I'm a bit hazy on the details of users in Postgres. I think
    # by default it tries to use a database user with the same username as the
    # Linux user, so in my case, it made sense to create a database user named
    # dave and grant it permission on everything and use it to create the
    # databases.

Then go create a main/local_settings.py file and put something like this in it

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'davebase',
            'USER': 'dave',
            'PASSWORD': 'asdf1234',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
