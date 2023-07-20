try:
    import boto3
    import logging
    from botocore.exceptions import ClientError
    import os
    import uuid

except Exception as e:
    print('Error - libraries: {}'.format(e))

FILE_PATH = "D:/Study Materials/My git projects/Aws-prac/"
BUCKET_NAME = 'junn-test-glue'

s3_client = boto3.client('s3')

def get_files():
    try:
        all_file_names = [f for f in os.listdir(FILE_PATH) if f.endswith('.csv')]
        return all_file_names
    except Exception as e:
        print("Error - get_files: {}".format(e))

def upload_to_bucket():
    try:
       # To do: function to check if the file is stored already
        all_file_names = get_files()
        for file in all_file_names:
            obj_name= str(os.path.basename(file))
            print("uploading file - {}".format(obj_name))
            response= s3_client.upload_file(
                                FILE_PATH+'/'+obj_name,
                                Bucket=BUCKET_NAME,
                                Key=obj_name
        )   
            print("uploaded file - {}".format(obj_name))
    except ClientError as e:
        logging.error(e)
        return False
    return True

upload_to_bucket()

