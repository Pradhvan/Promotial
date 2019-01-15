# Promotial
A web app for managing marketing campaigns. 

### Frontend

- [x] Login screen with email and password

- [x] On successful login, user should be redirected to a page having an "Add Rule" button which allows user to create a new rule through a modal (like a contact form). The Create Rule modal must have following things:-

    - [x] Rule name

    - [x] Campaigns - to which campaign, should the rule be attached (multiselect field)

    - [x] Schedule - at what time should this rule be triggered

    - [x] Conditions - text box in which rules can be specfied

    - [x] Action - actions that needs to be taken

    - [x] Status - Activated/Deactivated

- [x] The same page should have a table of all the rules that has been created by the user. Each rule line in the table should specify Rule name, Campaigns, Rule Schedule, Rule Status (Activated/Deactivated) and an edit button. 

- [x] The edit button opens the same Create Rule modal but with data filled according to the specific rule.

### Backend 

- [x] Rule executor service

   - [x]  The service should run every 15 minutes

    - [ ] It should check for rules that must be executed according to schedule

    - [ ] If the rule should be executed, make a lookup for data and execute the condition in the rule and trigger congiured action.

- [x] Action executor service

    - [x] Implement Notify action only
 
 
## Devlopment Guide:

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

*Once the server runs sucessfully you would see this landing page, just add your superuser username and password*

<a href="https://ibb.co/XF6qrjQ"><img src="https://i.ibb.co/ygKrcd9/Screenshot-from-2019-01-15-14-52-37.png" alt="Screenshot-from-2019-01-15-14-52-37" border="0"></a>

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
