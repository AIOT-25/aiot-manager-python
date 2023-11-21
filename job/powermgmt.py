"""
powermgmt
=============
WISE-4012로부터 Sensor 데이터 수집 및 데이터 notify 하는 역할 수행
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

  def job(self):
    log("Job start")

    while True:
      # 여기에 코드 작성할 것!!!!
      time.sleep(1)

  def start(self):
    threading.Thread(target=self.job).start()

  def __del__(self):
     self.__notifier.unregister(self)   
