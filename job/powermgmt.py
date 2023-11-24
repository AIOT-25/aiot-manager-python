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
  def __init__(self, notifier, serialController):
     self.__notifier = notifier
     self.__model = model_loader.model_loader()
     self.__flow_datas = []
     self.__time_zones = []
     self.__serialController = serialController
     notifier.register(self)

  def notify(self, values):
    if len(self.__flow_datas) == 10 and len(self.__time_zones) == 10:
        # predict 수행
        if self.__model.load_model():
            result = self.__model.predict([self.__flow_datas, self.__time_zones])
            motor_speed = math.ceil(result * 9.8)
            serialController.send(str(motor_speed))
        self.__flow_datas = []
        self.__time_zones = []
        
        
    self.__flow_datas.append(values[0])
    self.__time_zones.append(values[3])


  def __del__(self):
     self.__notifier.unregister(self)   
