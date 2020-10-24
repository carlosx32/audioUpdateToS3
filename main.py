
import uuid
from resources.recorder import recorder
from resources.awsS3Resource import AwsS3Resource
from resources.deviceInfo import deviceInfo


while True:
    awsS3 = AwsS3Resource()
    device=deviceInfo()
    info=device.getInfoObj()

    ext=".wav"
    filename=uuid.uuid1().__str__()
    metadata={"audio_filename": filename, "device_info":info}
    grabador=recorder(dirname='audiostemp')
    ruta=grabador.record(id=filename)
    AwsS3Resource.uploadData(awsS3,file_name=ruta,object_s3_name=filename+ext,dicMetadata=metadata)