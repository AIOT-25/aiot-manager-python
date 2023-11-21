import threading
import time
from util.logger import log
from protocol.modbus import ModbusClient

def wait_init_sensor_thread(event):
   log("Sensor Thread Init 대기 중...")
   while not event.is_set():
      time.sleep(1)
      
def job(c, event_thread_stop, event_init_sensor_thread):
    # 센서 스레드 기동 대기
    wait_init_sensor_thread(event_init_sensor_thread)
    
    log("Job start")

    while not event_thread_stop.is_set():
      # 여기에 코드 작성할 것!!!!
      time.sleep(1)

    log("Job Finish")

def get_power_mgmt_thread(config, event_thread_stop, event_init_sensor_thread):
  return threading.Thread(target=job, args=(config, event_thread_stop, event_init_sensor_thread))