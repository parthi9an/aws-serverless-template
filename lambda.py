import json
import boto3
import uuid 

def list_announcements(event, context):
  # TODO implement
  dynamodb = boto3.resource('dynamodb')
  tableAnnouncements = dynamodb.Table('Announcements')
  response = tableAnnouncements.scan()
  return {
    'statusCode': 200,
    'body': response['Items']
  }

def create_announcement(event, context):
    # Instanciating connection objects with DynamoDB using boto3 dependency
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    # Getting the table the table Announcements object
    tableAnnouncement = dynamodb.Table('Announcements')
	id = event['id']
    title = event['title']
    description = event['description']
    date = event['date']
    # Putting a try/catch to log to user when some error occurs
    try:
        tableAnnouncement.put_item(
           Item={
			    'AnnouncementId' : id,
                'Title': title,
                'Description': description,
                'Date': date
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Succesfully inserted Announcements!')
        }
    except:
        print('Closing lambda function')
        return {
                'statusCode': 400,
                'body': json.dumps('Error saving the Announcements')
        }  