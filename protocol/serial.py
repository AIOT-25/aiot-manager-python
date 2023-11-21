import serial

DEFAULT_BAUDRATE = 9600
DEFAULT_TIMEOUT = 0
class SerialController:
  def __init__(self, port, baudrate = DEFAULT_BAUDRATE, timeout = DEFAULT_TIMEOUT):
    self.port = port
    self.baudrate = baudrate
    self.timeout = timeout
    self.serial = None

  def is_connected(self):
    return not self.serial == None and self.serial.is_open

  def connect(self):
    try:
      self.serial = serial.Serial(
        port = self.port,
        baudrate = self.baudrate
      )
    except Exception as ex:
      print(f"Serial Connection Failed : {ex}")
      return False
    return True
  
  def close(self):
    if not self.is_connected():
      return
    self.serial.close()
  
  def send(self, str):
    if not self.is_connected():
      print("Please Connect Serial First.")
      return False
    self.serial.write(str.encode())
    return True
  
  def get_serial(self):
    return self.serial

  def readline(self):
    if not self.is_connected():
      print("Please Connect Serial First.")
      return
    return self.serial.readline().decode()
      