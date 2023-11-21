import threading
import time
from protocol.modbus import ModbusClientFactory, DUMMY
from util.logger import Logger
from job.datacollector import get_collect_sensor_data_thread
from job.powermgmt import get_power_mgmt_thread
from config import ManagerConfig

c = ManagerConfig()

# Sensor Thread 기동 여부 Flag
flag_init_sensor_thread = threading.Event()
# 모든 Thread 정지 위한 Flag
flag_thread_stop = threading.Event()

if __name__ == '__main__':
  Logger.create_logger()

  modbusClient = ModbusClientFactory.get_client(DUMMY, c.get_modbus_config())

  sensor_thread = get_collect_sensor_data_thread(modbusClient, flag_thread_stop, flag_init_sensor_thread)
  power_management_thread = get_power_mgmt_thread(c, flag_thread_stop, flag_init_sensor_thread)

  sensor_thread.start()
  power_management_thread.start()