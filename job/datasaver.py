"""
datasaver
=============
Data Notifier로 부터 전달받은 센서 데이터를 Datahub에 저장하는 역할 수행
"""
import threading
import time
from util.logger import log
from wisepaas.wisepaas import WisePaas

class SensorDataSaver:
  def __init__(self, config, notifier):
    self.__config = config
    self.__notifier = notifier
    notifier.register(self)
    
  def notify(self, value):
    print(f"Data Saver: {value}")

  def __job(self):
      log("Job start")

      while True:
        # 여기에 코드 작성할 것!!!!
        time.sleep(1)

  def start(self):
    threading.Thread(target=self.__job).start()

  def __del__(self):
    self.__notifier.unregister(self)
    