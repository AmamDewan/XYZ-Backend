### Instructions

* Clone Repo
```
git clone https://github.com/AmamDewan/InNeed-Backend
```
```
cd InNeed-Backend
```
* Create virtual environment(optional)
```
python -m venv venv
source venv/bin/activate
```
* Install required package 
```
pip install -r requirements.txt
```
__Rename__ `.env.example` to `.env` and set the necessary variables if needed

* database migration and create super user
```
python manage.py migrate
python manage.py createsuperuser
```

* Run the backend server

```shell
python manage.py runserver
```
\
_**Note:** do not use conda environment_
