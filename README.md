This repository houses the backend code for our IoT device that provides real-time power usage monitoring and introduces the concept of power sharing among neighbors. This README will guide you through the setup and usage of the backend system.

## Project Overview
The Nexus Interface Unit is an IoT device designed to revolutionize the way users monitor and manage their power consumption.<br/>
 Here are some key features of our device:<br/>
 
- Real-time Power Usage Monitoring: The device offers real-time monitoring of power consumption, allowing users to track their electricity usage efficiently.<br/>
- Power Capacity Insights: Users can gain valuable insights into the available power capacity, enabling them to make informed decisions about their energy consumption. <br/>
- Power Sharing: In situations where electricity resources are limited, our device introduces an innovative feature that enables power sharing among neighbors. This promotes energy efficiency and collaboration within communities.

## Backend Features
The backend of the Nexus Interface Unit Backend is responsible for handling and serving data to the frontend dashboard. Here are the core features of our backend system:
- Dashboard Data: The backend provides data for the dashboard, including power consumption statistics, customer information, and meter status (active or inactive).
- API Endpoints: We have defined API endpoints that allow communication between the frontend and backend systems. These endpoints enable data retrieval and manipulation for the dashboard.
-  Processing: Our backend system processes and aggregates data from the IoT devices, ensuring that accurate and up-to-date information is available on the dashboard.

## Technologies used
1. Django Framework: A web framework for building scalable web applications
2. PostgreSQL: Database Management System
3. Python: A programming language for your project


## Getting Started

- To set up and run the Nexus Interface Unit Backend on your local development environment, 
Follow these steps:

1. Begin by cloning this repository to your local machine using the git clone command.
```
git clone https://github.com/yourusername/nexus-backend.git
```
2. Navigate to the project directory
```
cd nexus-backend
```
3. Install the required dependencies. We recommend using a virtual environment for this step.
```
python3 -m venv venv
```
4. Activate the virtual environment using:
```
source venv/bin/activate
```

5.  Install Project Dependencies using:
```
pip install -r requirements.txt
```
6. Check the installed dependancies using:
```
pip freeze
``` 
7.  Install Psycopg2
```
pip install psycopg2
```
8.  Install Psycopg2-binary
 ```
pip install psycopg2-binary
```
9. Access PostgreSQL Database Console as "postgres" User
```
sudo -u postgres psql
```
10. Create the Database ,User and password in the postgres
11. Grant all priviledges on database to the user created .Use:
```
GRANT ALL PRIVILEGES ON DATABASE 'database_name' to 'database_user'
```
12. Make migrations using:
```
python3 manage.py makemigrations
```
13. Migrate using :
```
python3 manage.py migrate
```  
14. Runserver using:
 ```
python3 manage.py runserver
```
   
