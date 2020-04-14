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
    git pull upstream master  # Any time you want to pull rom davebase
    git push  # Any time you want to push to my-new-repo
