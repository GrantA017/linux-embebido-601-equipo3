

PORT = '/dev/tty.wlan-debug' #SOLO ES UN EJEMPLO

import time
import serial

arduino = serial.Serial(
    port=PORT,
    baudrate=BAUDRATE
)
arduino.write(b'hola')
time.sleep(.5)
received = arduino.readline()
print(received)
time.sleep(.5)
received = arduino.readline()
print(received)

for i in range(1, 4):
    to_send = f"Prueba {i}"
    arduino.write(to_send.encode(encoding="utf-8"))
    print("Enviado: {to_send}")
    time.sleep(.5)
    received = arduino.readline()
    print(f"Recibido: {received}")