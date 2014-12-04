Quick setup — if you've done this kind of thing before
or
HTTP https://github.com/daibaan/python.git
SSH  git@github.com:daibaan/python.git

We recommend every repository include a README, LICENSE, and .gitignore.
…or create a new repository on the command line

git config --global user.name Daibaan
git config --global user.email daibaan@daibaan.org
git config --global credential.helper cache
git config color.ui true

touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/daibaan/python.git
git push -u origin master
git status
