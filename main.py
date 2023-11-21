import threading
from protocol.modbus import ModbusClientFactory, DUMMY
from util.logger import Logger
from job.datanotifier import SensorDataNotifier
from job.powermgmt import PowerManagement
from job.datasaver import SensorDataSaver
from config import ManagerConfig

c = ManagerConfig()

# Sensor Thread 기동 여부 Flag
flag_init_sensor_thread = threading.Event()
# 모든 Thread 정지 위한 Flag
flag_thread_stop = threading.Event()

if __name__ == '__main__':
  Logger.create_logger()

  modbusClient = ModbusClientFactory.get_client(DUMMY, c.get_modbus_config())

  notifier = SensorDataNotifier(modbusClient)
  notifier.start()

  datasaver = SensorDataSaver(c, notifier)
  datasaver.start()

  powermgmt = PowerManagement(notifier)
  powermgmt.start()