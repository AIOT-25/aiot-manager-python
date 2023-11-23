"""
datacollector
=============
WISE-4012로부터 Sensor 데이터 수집 및 데이터 notify 하는 역할 수행
"""

import threading
import time
from util.logger import log
import random


class ModbusSensorDataNotifier:
  def __init__(self, client):
    self.__client = client
    self.__observers = []

  def register(self, observer):
    self.__observers.append(observer)

  def unregister(self, observer):
    self.__observers.remove(observer)

  def __read_sensor_data(self):
    regs = self.__client.get_client().read_holding_registers(0, 5)
    return [regs[0], regs[1], regs[2], 12, regs[2] * 12] 

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

class SerialSensorDataNotifier:
  def __init__(self, serialController):
    self.__controller = serialController
    self.__observers = []

  def register(self, observer):
    self.__observers.append(observer)

  def unregister(self, observer):
    self.__observers.remove(observer)

  def __read_sensor_data(self):
    try:
      splited = self.__controller.readline().split(" ")
      return [float(splited[0]), float(splited[1]), int(splited[2].replace("\r\n", ""))]
    except:
      return None

  def __job(self, event_thread_stop):
    log("Serial 연결 중...")
    if not self.__controller.connect():
      log("Serial 연결에 실패하였습니다. Port를 확인해주세요.")
      return

    log("Job start")
    while not event_thread_stop.is_set():
      sensor_data = self.__read_sensor_data()
      if not sensor_data == None:
        for observer in self.__observers:
          observer.notify(sensor_data)
      time.sleep(0.5)

  def start(self, event_thread_stop):
    threading.Thread(target=self.__job, args={ event_thread_stop }).start()
