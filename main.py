import threading
from protocol.modbus import ModbusClient
from wisepaas.wisepaas import WisePaasClient
from util.logger import Logger
from job.datanotifier import SensorDataNotifier
from job.powermgmt import PowerManagement
from job.datasaver import SensorDataSaver
from job.seriallistener import SerialListener
from config import ManagerConfig

c = ManagerConfig()

# Sensor Thread 기동 여부 Flag
flag_init_sensor_thread = threading.Event()
# 모든 Thread 정지 위한 Flag
flag_thread_stop = threading.Event()

if __name__ == '__main__':
  try:
    Logger.create_logger()

    modbusClient = ModbusClient(c.get_modbus_config())
    wisepaasClient = WisePaasClient(c.get_wisepaas_config())

    notifier = SensorDataNotifier(modbusClient)
    notifier.start(flag_thread_stop)

    datasaver = SensorDataSaver(wisepaasClient, c, notifier)
    powermgmt = PowerManagement(notifier)

    seriallistener = SerialListener()
    seriallistener.start()
  except Exception as ex:
    flag_thread_stop.set()
    print("프로그램 실행 중 오류가 발생하였습니다.")
    exit(0)