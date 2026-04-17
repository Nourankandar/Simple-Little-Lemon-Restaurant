Project Title: Little Lemon Restaurant API - Capstone Submission

Description:
This project is a Django-based REST API for managing restaurant table bookings 
connected to a MySQL database.

API Paths for Testing (Important for Reviewers):
----------------------------------------------
1. Table Bookings Endpoint:
   URL: http://127.0.0.1:8000/api/bookings/
   Methods: GET, POST
   (Note: Use this to view all bookings or create a new reservation)

2. User Registration & Authentication:
   URL: http://127.0.0.1:8000/api/registration/users/
   Methods: POST
   (Note: Use this to register a new user for the system)

3. Token Generation (Login):
   URL: http://127.0.0.1:8000/api/registration/token/login/
   Methods: POST
   (Note: This provides the Auth Token needed for secure requests)

Setup Instructions:
------------------
1. Database: Ensure MySQL is running and a database named 'little_lemon_db' exists.
2. Dependencies: Run 'pip install django djangorestframework mysqlclient djoser python-dotenv'.
3. Migrations: Run 'python manage.py migrate'.
4. Server: Run 'python manage.py runserver'.

Testing with Insomnia/Postman:
-----------------------------
- To access protected routes, include the following in the Header:
  Key: Authorization
  Value: Token <your_generated_token>


