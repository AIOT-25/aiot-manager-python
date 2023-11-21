"""
datasaver
=============
Data Notifier로 부터 전달받은 센서 데이터를 Datahub에 저장하는 역할 수행
"""
from util.logger import log

class SensorDataSaver:
  def __init__(self, client, config, notifier):
    self.__client = client
    self.__client.connect()

    self.__config = config
    self.__notifier = notifier
    notifier.register(self)
    
    
  def notify(self, value):
    self.__client.save_edge_data(value)

  def __del__(self):
    self.__notifier.unregister(self)
    