import threading
import time

class SerialListener:

  def __job(self):
    while True:
      time.sleep(1)      

  def start(self):
    th = threading.Thread(target=self.__job)
    th.start()