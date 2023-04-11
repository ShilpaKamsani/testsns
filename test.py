import boto3

# Create an SNS client
sns = boto3.client('sns')

# Create a topic
response = sns.create_topic(Name='my-topic')

# Get the ARN of the topic
topic_arn = response['TopicArn']

# Add an email subscriber to the topic
response = sns.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint='shilpakamsani98@gmail.com'
)

# Print the subscription ARN
print(response['SubscriptionArn'])
