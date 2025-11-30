My Django Project
===================

Overview
--------

A portfolio website, showcasing several of my projects, my work history, and some general information about myself.  
Made as a showcase of my programming experience itself, this website is also in my projects list.

Technologies Used
------------------

- Python
- Django
- Vue.js
- Docker
- Docker Compose

Getting Started
---------------

- Local development
  1. Ensure Python is installed
  2. Install Django: `pip install django`
  3. Clone the repository: `git clone <repository_url>`
  4. Navigate to the project directory and create a virtual environment: `python -m venv venv && source venv/bin/activate`
  5. Install the project's dependencies: `pip install -r requirements.txt`
  6. Start the development server: `python manage.py runserver runserver`
- Production deployment
  1. Clone repo
  2. Build docker image: `docker build -t portfolio .`
  3. Start container: `docker run -d portfolio`
  4. Point web server (NGINX, Apache, etc.) at localhost:8000

License
-------

This project is licensed under [Apache-2.0 license](NOTICE).