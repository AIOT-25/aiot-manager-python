"""
datacollector
=============
WISE-4012로부터 Sensor 데이터 수집 및 데이터 notify 하는 역할 수행
"""

import threading
import time
from util.logger import log
import random


class SensorDataNotifier:
  def __init__(self, client):
    self.__client = client
    self.__observers = []

  def register(self, observer):
    self.__observers.append(observer)

  def unregister(self, observer):
    self.__observers.remove(observer)

  def __read_sensor_data(self):
    return random.sample(range(1,11), 5)

  def __job(self, event_thread_stop):
    log("Modbus 연결 중...")
    if not self.__client.open():
      log("Modbus 연결에 실패하였습니다. Host와 Port를 확인해주세요.")
      return

    log("Job start")
    while not event_thread_stop.is_set():
      for observer in self.__observers:
        observer.notify(self.__read_sensor_data())
      time.sleep(1)

  def start(self, event_thread_stop):
    threading.Thread(target=self.__job, args={ event_thread_stop }).start()

