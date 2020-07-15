# aws-serverless-template
Sample cloud formation template of Serverless services


# Prerequisites

1.  Either clone this repo with ``` git clone https://github.com/parthi9an/aws-serverless-template.git ``` or just download the [current zip file](https://github.com/parthi9an/aws-serverless-template/archive/master.zip) and extract it in an empty directory.

# Utilized services in AWS

	- IAM
	- Lambda
	- DynamoDB
	- S3
	- API Gateway
	- Cloud Formation
	
# Others
	- OpenAPI 3.0
	- Postman
 	

# Steps to reproduce

1. Create S3 bucket ```itc-lambda``` and upload the ```lambda.zip``` file.
	 - It contains lambda python handler of RestApis ```(ListAnnouncements, CreateAnnouncement)```
2. Upload the template ```itc-aws-iam-template.yml``` in AWS Cloud formation.
	 - This is used to create the Ueers,Groups,Policies, and Role for accessing the AWS resources.
	 
3. Upload the template ```itc-aws-dynamodb-template.yml``` in AWS Cloud formation.
	 - This is used to create dynamoDB table ```Announcements``` and associated policies, roles.
	 - Table contains the fields ```AnnouncementId, Title, Description, and Date```.

4. Upload the template ```itc-aws-serverless-cf-template.yml``` in AWS Cloud formation.
	 - This is used to define the RestApis (ListAnnouncements, CreateAnnouncement) along with lambda function, Permissions and Deployments
	 - API endpoints
		- ListAnnouncements - GET - [https://{ApiId}.execute-api.{aws-region}.amazonaws.com/Dev/announcements](https://{ApiId}.execute-api.{aws-region}.amazonaws.com/Dev/announcements)
		- CreateAnnouncement - POST - [https://{ApiId}.execute-api.{aws-region}.amazonaws.com/Dev/announcements](https://{ApiId}.execute-api.{aws-region}.amazonaws.com/Dev/announcements)
		
5. After successful deployment, time to test the RestApis
	 - Copy the ```ApiId``` of the APIs from the list page of API Gateway.
	 - Replace the ```ApiId``` and ```AWS region``` values in the postman-collection.json.
	 - Import the collection in Postman. 
	 - Use postman to request the APIs.