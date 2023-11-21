import pyModbusTCP.client

DUMMY = 0
REAL = 1

class ModbusClientFactory:
  @staticmethod
  def get_client(type, config):
    if type == DUMMY:
      return DummyModbusClient(config)
    else:
      return ModbusClient(config)

class ModbusClient:
  def __init__(self, config):
    self.config = config
    self.client = None

  def open(self):
    self.client = pyModbusTCP.client.ModbusClient(host=self.config["host"], port=self.config["port"], timeout=5)
    return self.client.open()

  def is_connected(self):
    return not self.client == None and self.client.is_connected()
  
class DummyModbusClient:
  def __init__(self, config):
    self.config = config
    self.client = None

  def open(self):
    return True

  def is_connected(self):
    return True