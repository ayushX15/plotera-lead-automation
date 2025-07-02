## Smart Lead & Site Visit Automation System for Plotera

A complete backend system to manage leads, automate site visit reminders via SMS, and track sales operations — built with Flask, MySQL, and Twilio.

## 📚 Table of Contents:

Features

Folder Structure

Tech Stack

Installation & Setup

API Endpoints

SMS Reminder System

Logging

Future Enhancements

Author



## ✨ Features:

✅ Lead Management: Create, update, and view leads with scheduled site visits.

✅ Salesperson Assignment: Easily assign sales staff to leads.

✅ Automated Reminders: Daily cron script to send SMS reminders to clients and salespersons.

✅ Secure Configuration: Uses .env to keep sensitive data safe.

✅ Logging: Records all activities and errors to logs/app.log.



## 🗂 Folder Structure:

plotera-lead-automation/
├── app.py               # Entry point for Flask app
├── config.py            # Loads environment & DB config
├── .env                 # Secrets (Twilio, DB)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── .gitignore           # Ignore __pycache__, .env, etc.

├── db/
│   ├── db_connection.py # MySQL connection function
│   └── init_db.sql      # Creates DB, tables, test data

├── routes/
│   ├── leads.py         # API routes for leads
│   └── sales.py         # API routes for salespersons

├── utils/
│   └── sms.py           # Sends SMS using Twilio

├── cron/
│   └── send_reminders.py # Checks today's visits & sends SMS

├── logs/
│   └── app.log          # Logs all actions

├── tests/
│   └── __init__.py      # Placeholder for tests



## ⚙ Tech Stack:

Backend: Python + Flask

Database: MySQL

SMS: Twilio API

Environment: dotenv

Logging: Python logging



## 🔧 Installation & Setup:

1️⃣ Clone / Download this repo

git clone https://github.com/ayushX15/plotera-lead-automation.git

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Set up MySQL database

Create the DB + tables by running init_db.sql: mysql -u root -p < db/init_db.sql

4️⃣ Configure your environment

DB_HOST=localhost

DB_USER=root

DB_PASSWORD=yourpassword

DB_NAME=plotera_db

TWILIO_SID=your_twilio_sid

TWILIO_AUTH_TOKEN=your_twilio_token

TWILIO_PHONE=+11234567890

5️⃣ Run the app

python app.py



## 🔗 API Endpoints:

## Endpoints----------Method-----------Description

    /ping	                    GET	            Check if server is running
    /test-db	            GET	            Check MySQL connection
    /add-lead	            POST        Add new lead
    /get-leads	            GET	            List all leads
    /get-today-visits	    GET	            Get today's scheduled visits
    /update-status	            PUT	            Update lead status
    /assign-salesperson	    PUT	            Assign salesperson to a lead

Test these using Postman or browser.



## 📡 SMS Reminder System:

✅ One-off test SMS

python send_test_sms.py

Sends a demo SMS to verify Twilio setup.

✅ Daily reminders

python cron/send_reminders.py

Fetches today's visits from DB.

Sends SMS to both client & salesperson.

Writes logs to logs/app.log.

## 📝 Logging:

All activities (like sent SMS, errors, cron runs) are logged into:

logs/app.log



## 🚀 Future Enhancements:

Email notifications

JWT Auth for API security

Admin dashboard

Docker + CI/CD pipeline

Unit & integration tests



## PREPARED BY:

🧑‍💻 Ayush Prasad
🧑‍💻 Chetan Kumar Rohilla

