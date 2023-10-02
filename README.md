# DSCRM: Django based CRM system 

CRM system for keeping records of customers and orders

## Installation and Usage

Here's how to get the project up and running on your local machine for development and testing.

### Prerequitements
<ul>
  <li>Python 3.11</li>  
  <li>Django 4</li>
  <li>PostgreSQL</li>
</ul>

<h3>Setup</h3>
<ol>
  <li>Clone this repository:</li>

    git clone git@github.com:gevorgar/dscrm.git
    
  <li>Navigate to the project directory:</li>


    cd dscrm

  <li>Install the project requirements:</li>

    pythot3 -m pip install -r requirements.txt
  <li>Create PostgreSQL database adn configure connection</li>
  <li>Make migrations and migrate</li>
  
    cd dscrm_service
    python3 manage.py makemigrations
    python3 manage.py migrate
  <li>Run the application:</li>

    python3 manage.py runserver
</ol>

Your application should now be running at `http://localhost:8000`.


