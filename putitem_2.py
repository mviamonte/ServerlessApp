import boto3
client = boto3.client('dynamodb')
response = client.put_item(
    TableName='PetsDB',
    Item={
        'ID': {
            'N': '2',
        },
        'PetName': {
            'S': 'Benito',
        },
        'PetType': {
            'S': 'Cat',
        },    
         'PetColour': {
            'S': 'Gray',
        }, 
         'Character': {
            'S': 'Annoying',
        }, 
},
ReturnConsumedCapacity='TOTAL',
)

print(response)