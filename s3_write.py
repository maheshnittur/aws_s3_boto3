import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
count = 1
for bucket in s3.buckets.all():
    print(bucket.name)
    s3.meta.client.upload_file('/home/ec2-user/hello.txt', 'maheshsample', 'hello.txt')
