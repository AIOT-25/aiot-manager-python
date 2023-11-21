from pyModbusTCP.client import ModbusClient

class ModbusClient:
  def __init__(self, config):
    self.config = config
    self.client = None

  def open(self):
    self.client = ModbusClient(self.config.host, self.config.port)
    self.client.open()

  def is_connected(self):
    return not self.client == None and self.client.is_connected()
  