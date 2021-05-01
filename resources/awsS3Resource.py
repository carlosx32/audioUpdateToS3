import json
from logging import error
import logging
import os
import boto3
import io

from botocore.exceptions import ClientError

class AwsS3Resource:
    def __init__(self):
        session = boto3.Session(aws_access_key_id =os.environ["AWS_KEY"],aws_secret_access_key = os.environ["AWS_SECRET"])
        s3 = session.resource('s3')
        self.bucket = s3.Bucket(os.environ["S3_BUCKET"])
    def getStreamData(self, file_name):
        object = self.bucket.Object(file_name)
        audioStream = io.BytesIO()
        object.download_fileobj(audioStream)
        return audioStream.getvalue()
    def uploadData(self,file_name,object_s3_name,dicMetadata={}):
        try: 
            self.bucket.upload_file(file_name,object_s3_name,
            ExtraArgs=  {'Metadata': dicMetadata}
            )
            os.remove(file_name)
        except ClientError as e:
            logging.error(e)
            return False
            

