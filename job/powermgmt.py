"""
powermgmt
=============
Data Notifier로부터 전달받은 센서 데이터를 이용하여 LSTM 모델에 넣어 모터 효율화하는 작업 수행
"""
from util.logger import log
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import math
from ai import model_loader as model_loader
from protocol.serial import SerialController

class PowerManagement:
  def __init__(self, notifier):
     self.__notifier = notifier
     self.__model = model_loader.model_loader()
     self.__flow_datas = []
     self.__time_zones = []
     notifier.register(self)

  def notify(self, value, time):
    if len(self.__datas) == 10 and len(self.__time_zones) == 10:
        # predict 수행
        if self.__model.load_model():
            result = self.__model.predict([self.__datas, self.__time_zones])
        self.__datas = []
        self.__time_zones = []
        # 모터 제어 코드?
        # 이게 flow -> moter 출력값 (올림 진행)
        moter_speed = math.ceil(result * 9.8)
        SerialController.send(str(moter_speed)) # 이거 모터 제어 코드 맞나?
    self.__datas.append(value)
    self.__time_zones.append(time)


  def __del__(self):
     self.__notifier.unregister(self)   
