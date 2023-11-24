import threading
import signal
import sys
import time
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
# signal handler flag
flag_signal_handler_on = threading.Event()

def signal_handler(sig, frame):
    if flag_signal_handler_on.is_set():
        return
    flag_signal_handler_on.set()
    flag_thread_stop.set()
    print("\nProgram will terminated...")
    time.sleep(3)
    sys.exit(0)

if __name__ == '__main__':
  signal.signal(signal.SIGINT, signal_handler)
  try:
    Logger.create_logger()

    serial_config = c.get_serial_config()
    serialController = SerialController(port=serial_config["port"], baudrate=serial_config["baudrate"])

    serial2_config = c.get_serial2_config()
    serialController2 = SerialController(port=serial2_config["port"], baudrate=serial2_config["baudrate"])

    wisepaasClient = WisePaasClient(c.get_wisepaas_config())

    notifier = SerialSensorDataNotifier(serialController)
    notifier.start(flag_thread_stop)

    datasaver = SensorDataSaver(wisepaasClient, c, notifier)
    powermgmt = PowerManagement(notifier, serialController2)

  except Exception as ex:
    print(ex)
    flag_thread_stop.set()
    print("프로그램 실행 중 오류가 발생하였습니다.")
    exit(0)
