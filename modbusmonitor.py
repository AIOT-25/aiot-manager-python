from config import ManagerConfig
from protocol.modbus import ModbusClient
import time

c = ManagerConfig()

modbusClient = ModbusClient(c.get_modbus_config())

count = 0
while not modbusClient.is_connected():
    modbusClient.open()
    if count > 5:
        print("Can't connect")
        exit(0)
    count += 1

while True:
    regs = modbusClient.get_client().read_holding_registers(0, 10)
    print(regs)
    time.sleep(0.5)
