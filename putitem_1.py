import boto3
client = boto3.client('dynamodb')
response = client.put_item(
    TableName='PetsDB',
    Item={
        'ID': {
            'N': '1',
        },
        'PetName': {
            'S': 'Bilbo',
        },
        'PetType': {
            'S': 'Cat',
        },    
         'PetColour': {
            'S': 'Black',
        }, 
         'Age': {
            'N': '4',
        }, 
},
ReturnConsumedCapacity='TOTAL',
)

print(response)