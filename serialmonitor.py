from protocol.serial import SerialController
import time

port = ""
while port == "":
    port = input("Please Input Serial Port : ")

baudrate = 0
while baudrate == 0:
    try:
        tempBaudrate = input("Please input baudrate : ")
        if tempBaudrate == "":
            baudrate = 9600
            break
        baudrate = int(tempBaudrate)
    except:
        print("Baudrate can be only number")

serialController = SerialController(port, baudrate)

count = 0
while not serialController.is_connected():
    serialController.connect();
    time.sleep(0.5)
    count += 1
    if count > 5:
         print(f"Can't connect to {port}. Please retry other port")
         exit(0)

while True:
    print(serialController.readline())