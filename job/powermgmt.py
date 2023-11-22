"""
powermgmt
=============
Data Notifier로부터 전달받은 센서 데이터를 이용하여 LSTM 모델에 넣어 모터 효율화하는 작업 수행
"""
import threading
import time
from util.logger import log
import model_loader

class PowerManagement:
  def __init__(self, notifier):
     self.__notifier = notifier
     notifier.register(self)

  def notify(self, value):
    print(f"Power Mgmt: {value}")
    # 모델 객체 생성
    m = model_loader.model_loader()
    # 임의로 만들어줌 나중에 매개변수 넣을 수 있으면 지워야함.
    input_list = []
    while True:
      # 여기에 코드 작성할 것!!!!
      # 모델 예측을 위해 인풋 리스트 필요함
      result = m.predict(input_list)
      return result

  def __job(self):
    log("Job start")


  def start(self):
    threading.Thread(target=self.__job).start()

  def __del__(self):
     self.__notifier.unregister(self)   
