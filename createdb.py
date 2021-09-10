import boto3
client = boto3.client('dynamodb')
response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'ID',
            'AttributeType': 'N'           
        },
        {
            'AttributeName': 'Customer',
            'AttributeType': 'S'           
        },
],
TableName= 'CustomerDB',
KeySchema=[
        {
            'AttributeName': 'ID',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Customer',
            'KeyType': 'RANGE'
        },
],
BillingMode='PROVISIONED',
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    },
    StreamSpecification={
        'StreamEnabled': False,
    },
    Tags=[
        {
            'Key': 'Name',
            'Value': 'TestingDB'
        },
    ]
)
