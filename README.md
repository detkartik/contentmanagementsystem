# Content Management System

Assignment project using Django &amp; DRF

### Project Setup for Mac

- Install python
  ```sh
  brew install python3
  ```
- Install postgres
  ```sh
  brew install postgres
  brew install postgresql
  ```
- Start postgres
  ```sh
  brew service start postgres
  ```
- Create db
  ```sh
  createdb contentdb
  ```
- Clone project
  ```sh
  git clone git@github.com:detkartik/contentmanagementsystem.git
  cd contentmanagementsystem/
  ```
- Create virtualenv
  ```sh
  brew install mkvirtualenv
  mkvirtualenv --python=/usr/local/bin/python3 cms
  workon cms
  ```
- Install packages
  ```sh
  pip install -r requirements.txt
  ```
- To run the project
  ```sh
  cd project
  python manage.py migrate
  python manage.py collectstatic
  python manage.py createsuperuser
  python manage.py runserver
  ```

### Project Setup for Ubuntu

- Install Python

```sh
Sudo apt install python3.7
```

- Install postgres

```sh
sudo apt install postgresql postgresql-contrib
sudo su postgres
createdb contentdb
```

- Clone project

```sh
git clone git@github.com:detkartik/contentmanagementsystem.git
cd contentmanagementsystem/
```

- Create virtualenv

```sh
sudo apt-get install python-pip
sudo pip install virtualenv
mkdir ~/.virtualenvs
sudo pip install virtualenvwrapper
export WORKON_HOME=~/.virtualenvs
. /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv cms
workon cms
pip install -r requirements.txt
```

- To run the project

```sh
cd project
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
python manage.py runserver
```
