import threading
import time
from util.logger import log

def job(client, event_thread_stop, event_init_sensor_thread):
  log("Modbus 연결 중...")
  if not client.open():
    log("Modbus 연결에 실패하였습니다. Host와 Port를 확인해주세요.")
    event_thread_stop.set()
    event_init_sensor_thread.set()
    return

  event_init_sensor_thread.set()

  log("Job start")
  while not event_thread_stop.is_set():
    time.sleep(1)
  log("Job Finish")

def get_collect_sensor_data_thread(client, event_thread_stop, event_init_sensor_thread):
  return threading.Thread(target=job, args=(client, event_thread_stop, event_init_sensor_thread))