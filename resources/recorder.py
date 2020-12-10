
import os,pyaudio,wave
from os.path import dirname

class recorder:
    def __init__(self,dirname,time=10):
        self.directory=dirname
        self.format=pyaudio.paInt16
        self.chanels=1
        self.rate=44100
        self.time=time
        self.chunkSize=1024*4
        try:
            os.mkdir(dirname)
        except:
            pass
    def record(self,id,ext=".wav"):
        APP_ROOT= os.path.dirname(os.path.abspath(__file__))
        
        WAVE_OUTPUT_FILENAME = os.path.join(self.directory,id+ext)
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
    def calcularLeqA():
        """
        docstring
        """
        return "";
