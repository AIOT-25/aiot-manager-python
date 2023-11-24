import yaml

CONFIG_FILE_PATH = "config.yaml"

class ManagerConfig:
  def __init__(self, config_file_path = CONFIG_FILE_PATH):
    with open(config_file_path) as f:
      self.config = yaml.load(f, Loader=yaml.FullLoader)

  def get_wisepaas_config(self):
    return self.config['wisepaas']

  def get_modbus_config(self):
    return self.config['modbus']
  
  def get_serial_config(self):
    return self.config['serial']

  def get_serial2_config(self):
    return self.config['serial2']
