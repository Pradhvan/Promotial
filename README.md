# Promotial
A web app for managing marketing campaigns. 


## Devlopment:

### Project Setup:

#### 1. Create & activate the virtual environment 

```Bash
python3 -m venv test
source test/bin/activate 
```
#### 2. Install the dependencies 

```BASH
pip install -r requirements.txt
```

#### 3. Create a super user & Run server: 

```BASH
python manage.py createsuperuser 
python manange.py runserver 
```

## Cronjob Setup:


#### 1. Schedule Cron Schedule

```python
CRONJOBS = [
    ('*/1 * * * *', 'rbengine.cron.my_scheduled_job',
     '>> /home/scheduled_job.log'),
]
```

#### 2. Add function to rbengine/cron.py

#### 3. Add cron job to the machine 

``` python
python manage.py crontab add . 
``` 

Run the **add** command everytime you update the cron job setup.This would update it in the machine. 

To *remove* cron job use: 

```python
python manage.py crontab remove
```