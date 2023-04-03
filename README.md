BNproject CRM App
This is a CRM application created by Ihor Halas for BNproject. The app retrieves data from an XLSX file in Google Sheets for the current date and sends a reminder message to clients about their appointments the next day.

In addition, the app also takes data about completed orders and adds it to the database in the Orders table. If a client is not already in the Clients table, the app creates a new entry and updates the table.

Features
Retrieves data from Google Sheets for the current date
Sends reminder messages to clients about their appointments the next day
Adds completed order data to the Orders table in the database
Creates and updates client information in the Clients table in the database
Deployed on AWS EC2 with RDS using MySQL
Uses pipenv for dependency management
Sends SMS using turbosms service

Technologies Used
Python
Google Sheets API
TurboSMS API
MySQL
AWS EC2 and RDS
Pipenv

Requirements
Python 3
Google Sheets API credentials
Twilio API credentials
MySQL
AWS account
Pipenv

Installation
Clone the repository to your local machine
Create a virtual environment and activate it using pipenv
Install the required packages by running pipenv install
Obtain the required credentials for the Google Sheets API and the Twilio API
Create a .env file in the root directory and add the necessary credentials, using the .env.example file as a template
Configure your MySQL database on AWS RDS and update the database credentials in the .env file
Launch an AWS EC2 instance and clone the repository onto the instance
Run the app using python app.py

Usage
Run the app using python app.py
The app will retrieve the data from Google Sheets and send reminders to clients for their appointments the next day
The app will also add any completed order data to the Orders table in the database, and create or update the Clients table as necessary.

Contributing
Contributions are welcome! Please create a new branch for any changes and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.