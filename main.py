
import uuid
from resources.recorder import recorder
from resources.awsS3Resource import AwsS3Resource
from resources.deviceInfo import deviceInfo
from datetime import datetime
from dateutil import tz


while True:
    awsS3 = AwsS3Resource()
    device=deviceInfo()
    info=device.getInfoObj()
    filename="raspberry-"+uuid.uuid1().__str__()

    grabador=recorder(dirname='audiostemp',time=10)
    ruta=grabador.record(id=filename)

    now = datetime.now(tz=tz.tzutc())
    date_time = now.strftime("%Y-%m-%dT%H:%M:%S")
    info['audio_uuid'] = filename
    info['time'] = date_time
    AwsS3Resource.uploadData(awsS3,file_name=ruta,object_s3_name=filename,dicMetadata=info)
