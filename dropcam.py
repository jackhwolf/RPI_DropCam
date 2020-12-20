from time import time, sleep
import os
from io import BytesIO
from picamera import PiCamera

class DropCam:
    
    def __init__(self):
        self.c = None
        self._connect()

    def _connect(self):
        camera = PiCamera()
        camera.resolution = (1024, 768)
        camera.start_preview()
        sleep(2)
        self.c = camera
        
    def _disconnect(self):
        self.c = None
        
    def pic_to_stream(self):
        io = BytesIO()
        self.c.capture(io, 'jpeg')
        return io, 'jpeg'
    
    def pic_to_file(self):
        path = os.path.join('files', str(int(time()*1000)) + '.jpeg')
        self.c.capture(path)
        return path
    
    