import json
import os
import boto3
import io

class AwsS3Resource:

    def __init__(self):
        session = boto3.Session()
        s3 = session.resource('s3')
        self.bucket = s3.Bucket('audios-a-inferir')
    def getStreamData(self, file_name):
        object = self.bucket.Object(file_name)
        audioStream = io.BytesIO()
        object.download_fileobj(audioStream)
        return audioStream.getvalue()
    def uploadData(self,file_name,object_s3_name,dicMetadata={}):
        self.bucket.upload_file(file_name,object_s3_name,
        ExtraArgs=  {'Metadata':{
                        'audioData': json.dumps(dicMetadata),
                        }}
        )

