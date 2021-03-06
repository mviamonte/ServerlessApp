import boto3
client = boto3.client('dynamodb')
response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'ID',
            'AttributeType': 'N'           
        },

],
TableName= 'PetsDB',
KeySchema=[
        {
            'AttributeName': 'ID',
            'KeyType': 'HASH'
        },

],
BillingMode='PROVISIONED',
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
    StreamSpecification={
        'StreamEnabled': False,
    },
    Tags=[
        {
            'Key': 'Name',
            'Value': 'Pets'
        },
    ]
)
