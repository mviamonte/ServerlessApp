# ServerlessApp
In this first stage, my idea is have the front end using the s3 bucket who will be created using the *s3bucket.tf* code. (This file doesn't exists yet)
Still, is a testing of my little skills on serverless. This is a work in progress. 
The idea is create APIGateway / Lambda architecture to deploy two main functions. 
  -Create a register in an existing DB using DynamoDB
  -List all the registers in the Database. (Both functions are the ones showed at the index.html
  -The database will be previously created with some test registers. I need to change this to create the DynamoDB using Terraform 

## **Stage 1** --> Create the S3 site 
In the index.html there is a HTML template with two buttons. 
This index will be at the definition of the site using static site S3 feature. **@Andy** is going to "make up" a little bit the index.html 

## **Stage 2** --> Connect the index.html with the backend
How should I connect the functions  (backend) of my index.html. Using an HTTP API Gateway. The connection is direct from the bucket? (Event Driven?) For the moment, in the s3 static website configuration (the index.html bucket) I can add redirection rules pointing to API (HTTP) external URL(the actions or rules available in the API). Bottomline, I can redirect to another object within the bucket or to a external resource (URL), again, the ones available in the API Gateway.

## **Stage 3** --> The backend logic and the code
Backend "Logic"
  -The creation of the DB shall be configured using Terraform. Now I need to check the current code (Python)
  -Deploy the code to PUT information in the previously created database using DynamoDB. I had test a few options using the Python boto3. Haven't tested on Lambda. But the Python code for table creation is done and the put item is tested. Maybe I should include some update qty of items (just an idea).
  -Deploy the code to GET all the register from the DATABASE. Note, in some point, how to show the informatión will be a problem (maybe). 
 
There will be a fixed register for the new items, lambda functions will be deployed using Python SDK.

### **Some resources for the project**
#### Static web-site configuration (AWS) and website endpoints
https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html

https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteEndpoints.html

#### How to configure a index.html document
https://docs.aws.amazon.com/AmazonS3/latest/userguide/IndexDocumentSupport.html

#### Set permissions for S3 bucket
https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteAccessPermissionsReqd.html

#### Redirect and redirect rules examples
https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-page-redirect.html

https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-page-redirect.html#redirect-rule-examples

#### Terraform documentation
https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket

#### In case of emergency...
https://itnext.io/how-to-build-a-serverless-app-with-s3-and-lambda-in-15-minutes-b14eecd4ea89
