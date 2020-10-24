from logging import error
import logging
import os, requests
import socket

class deviceInfo:
    def __init__(self):
        self.deviceID=""
        self.location=[0,0]
        if( not os.environ.get('DEFAULTLAT')):
            os.environ['DEFAULTLAT']=str(4.2312)
            if( not os.environ.get('DEFAULTLONG')):
                os.environ['DEFAULTLONG']=str(72.2312)
            self.location=[os.environ.get('DEFAULTLAT'),os.environ.get('DEFAULTLONG')]
        if( not os.environ.get('DEVICEID')):
            self.deviceID=socket.gethostname()
            os.environ['DEVICEID']= self.deviceID
        if( not os.environ.get('DEVICEID')):
            os.environ['DEVICEINFO']="sin descripciòn"
        
    def getGeoData(self):
        self.location=[os.environ.get('DEFAULTLAT'),os.environ.get('DEFAULTLONG')]
        try:
            res = requests.get('https://ipinfo.io/')
            data = res.json()
            self.location = data['loc'].split(',')
        except error:
            logging.error(error)
        
        return self.location
    def getInfoObj(self):

        geodata = self.getGeoData()
        identifier = self.deviceID
        deviceInfo = { 
            "id":identifier ,
            "location-lon": geodata[0],
            "location-lat": geodata[1],
            "description": os.environ.get('DEVICEINFO')
        }
        return deviceInfo
    def getDeviceIdentifier(self):
        self.deviceID=os.environ.get('DEVICEID')
        return self.deviceID

