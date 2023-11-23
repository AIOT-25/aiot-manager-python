import pyModbusTCP.client

class ModbusClient:
  def __init__(self, config):
    self.config = config
    self.client = None

  def open(self):
    self.client = pyModbusTCP.client.ModbusClient(host=self.config["host"], port=self.config["port"], timeout=5)
    return self.client.open()

  def is_connected(self):
    return not self.client == None and self.client.is_open
  
  def get_client(self):
    return self.client
