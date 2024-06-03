from tkinter import *
from tkinter import Tk
from tkinter import Frame
from tkinter.ttk import Combobox
from tkinter import Button
from PIL import Image, ImageTk  # Importing PIL for image handling
import pygame # Pygame or sounds.
pygame.mixer.init()
# Seriales
from sensor_serial import BAUDRATES
from sensor_serial import SensorSerial
from utils import find_available_serial_ports
# Assets
back = "C:/Users/Grant/OneDrive/School & Courses/[S10] Diseño de Sistemas en Chip/Módulo 4 - Linux Embebido - Pedro/linux-embebido-601-equipo3/Ardu/Assets/Beige.png"
texture = "C:/Users/Grant/OneDrive/School & Courses/[S10] Diseño de Sistemas en Chip/Módulo 4 - Linux Embebido - Pedro/linux-embebido-601-equipo3/Ardu/Assets/Wood - (Dark Outdoors) (16,9).png"
button_sound = "C:/Users/Grant/OneDrive/School & Courses/[S10] Diseño de Sistemas en Chip/Módulo 4 - Linux Embebido - Pedro/linux-embebido-601-equipo3/Ardu/Assets/CHIME_FX_popper_01.mp3"

def play_sound(): # Play sound function.
    pygame.mixer.music.load(button_sound)
    pygame.mixer.music.play()
    
def create_serial_devices_combobox()-> Combobox:
        ports = find_available_serial_ports()
        return Combobox(values=ports, font=('Courier', 20))
    
def create_serial_devices_refresh_button() -> Button:
    return Button(
        text='Refresh available serial devices',
        command=refresh_serial_devices
    )
    
def create_baudrate_combobox() -> Combobox:
    return Combobox(
        values=['Baudrate'] + BAUDRATES
    )
    
def create_connect_serial_button() -> Button:
    return Button(
        text='Connect',
        command=create_sensor_serial
    )
    
def refresh_serial_devices():
    ports = find_available_serial_ports()
    serial_devices_combobox.selection_clear()
    serial_devices_combobox['values'] = ports
    
def create_sensor_serial()->SensorSerial:
    port = serial_devices_combobox.get()
    baudrate = baudrate_combobox.get()
    
    if port == '' or baudrate == 'Baudrate':
        raise ValueError(f'Incorrect values for {port=} {baudrate=}')
    
    sensor_serial = SensorSerial(
        port=port,
        baudrate=int(baudrate)
    )
    
def read_temperature() -> None:
    if sensor_serial is not None:
        temperature = sensor_serial.send('TC2')
        temperature_label['text'] = temperature[:-3]
        return
    raise RuntimeError("Serial connection has not been initialized")
    
if __name__ == '__main__':
    root = Tk()
    root.title = 'example'
    root.geometry('800x800')
    
    # Load the background image
    image_path = back
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    
    # GUI objects creationg
    serial_devices_combobox: Combobox = create_serial_devices_combobox()
    refresh_serial_devices_button : Button = create_serial_devices_refresh_button()
    baudrate_combobox : Combobox = create_baudrate_combobox()
    connect_serial_button: Button = create_connect_serial_button()
    # Other objects
    sensor_serial : SensorSerial | None = None
    
    # Row 0
    serial_devices_combobox.grid(row=0, column=0)
    refresh_serial_devices_button.grid(row=0, column=1)
    baudrate_combobox.grid(row=0, column=2)
    connect_serial_button.grid(row=0, column=3)
    # Settings
    baudrate_combobox.current(0)
    
    root.mainloop()