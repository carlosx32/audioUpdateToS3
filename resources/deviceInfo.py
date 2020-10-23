from logging import error
import logging
import os, requests
import socket

class deviceInfo:
    def __init__(self):
        if( not os.environ.get('DEFAULTLAT')):
            os.environ['DEFAULTLAT']=str(4.2312)
        if( not os.environ.get('DEFAULTLONG')):
            os.environ['DEFAULTLONG']=str(72.2312)
        if( not os.environ.get('DEVICEID')):
            os.environ['DEVICEID']= socket.gethostname()
        if( not os.environ.get('DEVICEID')):
            os.environ['DEVICEINFO']="sin descripciòn"
        
        
    def getGeoData(self):
        location=[os.environ.get('DEFAULTLAT'),os.environ.get('DEFAULTLONG')]
        try:
            res = requests.get('https://ipinfo.io/')
            data = res.json()
            location = data['loc'].split(',')
        except error:
            logging.error(error)
        return location
    def getDeviceIdentifier(self):
        return os.environ.get('DEVICEID')

    def getInfoObj(self):

        geodata = self.getGeoData()
        deviceInfo = { 
            "id": device.getDeviceIdentifier(),
            "location-lon": geodata[0],
            "location-lat": geodata[1],
            "description": os.environ.get('DEVICEINFO')
        }
        
        return deviceInfo