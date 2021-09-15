import boto3
client = boto3.client('dynamodb')
response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'ID',
            'AttributeType': 'N'           
        },
        {
            'AttributeName': 'PetName',
            'AttributeType': 'S'           
        },
        {
            'AttributeName': 'PetType',
            'AttributeType': 'S'           
        },
        {
            'AttributeName': 'PetColour',
            'AttributeType': 'S'
        },
],
TableName= 'PetsDB',
KeySchema=[
        {
            'AttributeName': 'ID',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'PetName',
            'KeyType': 'RANGE'
        },
        {
            'AttributeName': 'PetType',
            'KeyType': 'RANGE'
        },
        {
            'AttributeName': 'PetColour',
            'KeyType': 'RANGE'
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
