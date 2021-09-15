import boto3
response = client.put_item(
    TableName='CustomerDB',
    Item={
        'ID':{
            'N':'1',
        }
         'Customer':{
            'S':'Bilbo',
        }
    }
    
)