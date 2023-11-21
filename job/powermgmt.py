"""
powermgmt
=============
Data Notifier로부터 전달받은 센서 데이터를 이용하여 LSTM 모델에 넣어 모터 효율화하는 작업 수행
"""
import threading
import time
from util.logger import log

class PowerManagement:
  def __init__(self, notifier):
     self.__notifier = notifier
     notifier.register(self)

  def notify(self, value):
    print(f"Power Mgmt: {value}")

  def __job(self):
    log("Job start")

    while True:
      # 여기에 코드 작성할 것!!!!
      time.sleep(1)

  def start(self):
    threading.Thread(target=self.__job).start()

  def __del__(self):
     self.__notifier.unregister(self)   
