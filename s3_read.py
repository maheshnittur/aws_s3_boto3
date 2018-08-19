import boto3
#Git Repo add
# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
count = 1
for bucket in s3.buckets.all():
    print(bucket.name)
    for entries in bucket.objects.all():
        print( str(count) + " " + str(entries.key))
       # entries.delete()
       # print( " Object deleted : ")
        count += 1
