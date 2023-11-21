import threading
import time
from util.logger import log
from wisepaas.wisepaas import WisePaas

def wait_init_sensor_thread(event):
   log("Sensor Thread Init 대기 중...")
   while not event.is_set():
      time.sleep(1)

def job(c, event_thread_stop, event_init_sensor_thread):
    wait_init_sensor_thread(event_init_sensor_thread)

    log("Job start")

    while not event_thread_stop.is_set():
      # 여기에 코드 작성할 것!!!!
      time.sleep(1)
    print("Job Finish")

def get_collect_sensor_data_thread(config, event_thread_stop, event_init_sensor_thread):
  return threading.Thread(target=job, args=(config, event_thread_stop, event_init_sensor_thread))