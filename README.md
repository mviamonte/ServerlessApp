# ServerlessApp
In this first stage, my idea is have the front end using the s3 bucket who will be created using the *s3bucket.tf* code. 
Still, is a testing of my little skills on serverless. This is a work in progress. 
The idea is create API/Lambda functions to deploy two main functions. 
  -Create a register in an existing DB using DynamoDB
  -List all the registers in the Database. (Both functions are the ones showed at the index.html
  -The database will be previously created with some test registers. 

**Stage 1** --> Create the S3 site
In the index.html there is a HTML template with two buttons. 
This index will be at the definition of the site using static site S3 feature. **@Andy** is going to "make up" a little bit the index.html 

**Stage 2** --> Connect the index.html with the backend
How should I connect the functions  (backend) of my index.html. Using an internal API? HTTP API or REST? The connection is direct from the bucket?

**Stage 3** --> The backend logic and the code
Backend "Logic"
  -Deploy the code to PUT information in the previously created database using Dynamo.
  -Deploy the code to GET all the register from the DATABASE. Note, in some point, how to show the informatión will be a problem (maybe). 
 
There will be a fixed register for the new items, lambda functions will be deployed using Python SDK.
