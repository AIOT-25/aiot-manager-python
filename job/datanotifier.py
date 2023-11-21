"""
datacollector
=============
WISE-4012로부터 Sensor 데이터 수집 및 데이터 notify 하는 역할 수행
"""

import threading
import time
from util.logger import log

class SensorDataNotifier:
  def __init__(self, client):
    self.__client = client
    self.__observers = []

  def register(self, observer):
    self.__observers.append(observer)

  def unregister(self, observer):
    self.__observers.remove(observer)

  def job(self):
    log("Modbus 연결 중...")
    if not self.__client.open():
      log("Modbus 연결에 실패하였습니다. Host와 Port를 확인해주세요.")
      return

    log("Job start")
    while True:
      for observer in self.__observers:
        observer.notify("1")
      time.sleep(1)

  def start(self):
    threading.Thread(target=self.job).start()

