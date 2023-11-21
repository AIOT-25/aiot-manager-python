import threading
from protocol.modbus import ModbusClientFactory, DUMMY
from wisepaas.wisepaas import WisePaasClient
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
  wisepaasClient = WisePaasClient(c.get_wisepaas_config())

  notifier = SensorDataNotifier(modbusClient)
  notifier.start()

  datasaver = SensorDataSaver(wisepaasClient, c, notifier)
  powermgmt = PowerManagement(notifier)