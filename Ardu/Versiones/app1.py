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
back = "Assets/Beige.png"
texture = "Assets/Wood - (Dark Outdoors) (16,9).png"
button_sound = "Assets/CHIME_FX_popper_01.mp3"

class App(Frame):
    
    def __init__(self, master, *args, **kwargs)-> None:
        Frame.__init__(self, master, *args, **kwargs)
        self.master: Tk = master
        # GUI objects creation.
        self.serial_devices_combobox: Combobox = self.create_serial_devices_combobox()
        self.refresh_serial_devices_button : Button = self.create_serial_devices_refresh_button()
        self.baudrate_combobox : Combobox = self.create_baudrate_combobox()
        self.connect_serial_button: Button = self.create_connect_serial_button()
        # Other objects
        self.sensor_serial : SensorSerial | None = None
        self.init_gui()
        
    def  init_gui(self,)-> None:
        # GUI Config
        self.master.title = 'example'
        self.master.geometry('1200x800')
        self['bg'] = 'white'
        self.pack(fill='both', expand=True)
        
        # Row 0
        self.serial_devices_combobox.grid(row=0, column=0)
        self.refresh_serial_devices_button.grid(row=0, column=1)
        self.baudrate_combobox.grid(row=0, column=2)
        self.connect_serial_button.grid(row=0, column=3)
        
        # Settings
        self.baudrate_combobox.current(0)
        
    def create_serial_devices_combobox(self)-> Combobox:
        ports = find_available_serial_ports()
        return Combobox(self, values=ports, font=('Courier', 20))
    
    def create_serial_devices_refresh_button(self) -> Button:
        return Button(
            self,
            text='Refresh available serial devices',
            command=self.refresh_serial_devices
        )
        
    def create_baudrate_combobox(self,) -> Combobox:
        return Combobox(
            master=self,
            values=['Baudrate'] + BAUDRATES
        )
        
    def create_connect_serial_button(self) -> Button:
        return Button(
            master=self,
            text='Connect',
            command=self.create_sensor_serial
        )
        
    def refresh_serial_devices(self):
        ports = find_available_serial_ports()
        self.serial_devices_combobox.selection_clear()
        self.serial_devices_combobox['values'] = ports
        
    def create_sensor_serial(self)->SensorSerial:
        port = self.serial_devices_combobox.get()
        baudrate = self.baudrate_combobox.get()
        
        if port == '' or baudrate == 'Baudrate':
            raise ValueError(f'Incorrect values for {port=} {baudrate=}')
        
        self.sensor_serial = SensorSerial(
            port=port,
            baudrate=int(baudrate)
        )
        
    def read_temperature(self) -> None:
        if self.sensor_serial is not None:
            temperature = self.sensor_serial.send('TC2')
            self.temperature_label['text'] = temperature[:-3]
            return
        raise RuntimeError("Serial connection has not been initialized")
            

root = Tk()

if __name__ == '__main__':
    app = App(root)
    root.mainloop()