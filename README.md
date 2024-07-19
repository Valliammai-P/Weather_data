**Problem 1: Data Modeling**

Choosing PostgreSQL for this exercise due to its robustness and advanced features. The sql data definition for the weather data is in the data_modeling.sql file. 

**Problem 2: Ingestion**

For this, create a Python script - ingestion.py to ingest the data from the provided text files into the PostgreSQL database. Using SQLAlchemy for ORM and logging for tracking the process.

**Problem 3: Data Analysis**

Next, calculating the required statistics and store them in a new table ( data_analysis.sql)

**Problem 4: REST API**

Using Flask and Flask-RESTful to create the REST API in resapi.py

**Deployment**

For deploying on AWS, I would use the following approach:

    1. API and Web Server: Deploy the Flask application using AWS Elastic Beanstalk or ECS for better scalability.
    2. Database: Use Amazon RDS for PostgreSQL to manage the database.
    3. Scheduled Ingestion: Use AWS Lambda for running the data ingestion script periodically. This can be triggered by a CloudWatch Events rule.
    4. API Documentation: Use API Gateway to provide a single entry point for the API, which can also generate documentation from the Swagger/OpenAPI specification.

This setup ensures a scalable, reliable, and easy-to-manage infrastructure for the weather data API.
