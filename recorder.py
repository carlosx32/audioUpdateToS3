
import os,pyaudio,wave,uuid
from os.path import dirname
from resources.awsS3Resource import AwsS3Resource
from resources.deviceInfo import deviceInfo


class recorder:
    def __init__(self,dirname,ext=".wav"):
        self.directory=dirname
        self.ext=ext
        self.format=pyaudio.paInt16
        self.chanels=1
        self.rate=44100
        self.time=5 
        self.chunkSize=1024
        try:
            os.mkdir(dirname)
        except:
            pass
    def record(self,id):
        APP_ROOT= os.path.dirname(os.path.abspath(__file__))
        WAVE_OUTPUT_FILENAME = os.path.join(APP_ROOT, self.directory,id+self.ext)
        p = pyaudio.PyAudio()
        stream = p.open(format=self.format,
                        channels=self.chanels,
                        rate=self.rate,
                        input=True,
                        frames_per_buffer=self.chunkSize)

        print("* recording")
        frames = []
        for i in range(0, int(self.rate / self.chunkSize * self.time)):
            data = stream.read(self.chunkSize)
            frames.append(data)
        print("* done recording")
        stream.stop_stream()
        stream.close()
        p.terminate()   
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.chanels)
        wf.setsampwidth(p.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()

        return  WAVE_OUTPUT_FILENAME



awsS3 = AwsS3Resource()
device=deviceInfo()

ext=".wav"
filename=uuid.uuid1().__str__()+ext

metadata={"audio_filename": filename, "device_info":deviceInfo.getInfoObj()}

grabador=recorder(dirname='audiostemp')
ruta=grabador.record(id=filename)

AwsS3Resource.uploadData(awsS3,file_name=ruta,object_s3_name=filename,dicMetadata=metadata)