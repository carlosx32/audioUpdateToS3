import os,boto3,pyaudio,wave,uuid
from botocore.exceptions import ClientError
import logging

def record(id,directory,chunkSize=1024,format=pyaudio.paInt16,chanels=2,rate=44100,time=5,ext=".wav"):
    APP_ROOT= os.path.dirname(os.path.abspath(__file__))
    CHUNK = chunkSize
    FORMAT = format
    CHANNELS = chanels
    RATE = rate
    RECORD_SECONDS = time
    WAVE_OUTPUT_FILENAME = os.path.join(APP_ROOT, directory,id+ext)
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return  WAVE_OUTPUT_FILENAME

def uploadToBoto3(file_name,bucket,object_s3_name):
    s3=boto3.client('s3',region_name="us-east-1",aws_access_key_id ="AKIA4BM2RUPO6OLKDPDE",aws_secret_access_key ="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")
    try:
        response = s3.upload_file(file_name, bucket,object_s3_name,
        ExtraArgs=  {'Metadata':{
                        'dato': 'valor123',
                        'dato2': 'valor3231',
                        }
                    }       
        )
       
        os.remove(file_name)
    except ClientError as e:
        logging.error(e)
        return False


    dirname='audiostemp'
    try:
        os.mkdir(dirname)
    except:
        pass

    filename=uuid.uuid1().__str__()
    ext=".wav"
    ruta=record(id=filename,directory=dirname)
    uploadToBoto3(file_name=ruta,bucket='audios-a-inferir',object_s3_name=filename+ext)