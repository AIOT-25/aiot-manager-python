"""
powermgmt
=============
Data Notifier로부터 전달받은 센서 데이터를 이용하여 LSTM 모델에 넣어 모터 효율화하는 작업 수행
"""
from util.logger import log
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ai import model_loader as model_loader

class PowerManagement:
  def __init__(self, notifier):
     self.__notifier = notifier
     self.__model = model_loader.model_loader()
     notifier.register(self)

  def notify(self, value):
    # 임의로 만들어줌 나중에 매개변수 넣을 수 있으면 지워야함.
    input_list = []
    if self.__model.load_model():
      self.__model.predict(input_list)

  def __del__(self):
     self.__notifier.unregister(self)   
