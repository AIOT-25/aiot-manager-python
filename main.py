import threading
from protocol.serial import SerialController
from wisepaas.wisepaas import WisePaasClient
from util.logger import Logger
from job.datanotifier import SerialSensorDataNotifier
from job.powermgmt import PowerManagement
from job.datasaver import SensorDataSaver
from config import ManagerConfig

c = ManagerConfig()

# Sensor Thread 기동 여부 Flag
flag_init_sensor_thread = threading.Event()
# 모든 Thread 정지 위한 Flag
flag_thread_stop = threading.Event()

if __name__ == '__main__':
  try:
    Logger.create_logger()

    serial_config = c.get_serial_config()
    serialController = SerialController(port=serial_config["port"], baudrate=serial_config["baudrate"])

    wisepaasClient = WisePaasClient(c.get_wisepaas_config())

    notifier = SerialSensorDataNotifier(serialController)
    notifier.start(flag_thread_stop)

    datasaver = SensorDataSaver(wisepaasClient, c, notifier)
    powermgmt = PowerManagement(notifier)

  except Exception as ex:
    print(ex)
    flag_thread_stop.set()
    print("프로그램 실행 중 오류가 발생하였습니다.")
    exit(0)