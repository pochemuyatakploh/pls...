import subprocess
import traceback
from time import sleep
from kivy.uix.relativelayout import RelativeLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivymd.uix.list import OneLineListItem
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.button import Button
from threading import Thread
from kivy.clock import Clock
import bluetooth
import threading
from PyQt5 import QtBluetooth
Window.size = (480,853)
mutex = threading.Lock()

class Container(BoxLayout):

    def __init__(self):
        super().__init__()
        self.tr1 = Thread(target=self.devices())
        self.tr1.start()
        self.sock.connected.connect(self.connectedToBluetooth)


    def devices(self):
        self.sock = QtBluetooth.QBluetoothSocket(QtBluetooth.QBluetoothServiceInfo.RfcommProtocol)
        port = 1
        self.sock.connectToService(QtBluetooth.QBluetoothAddress("98:D3:39:30:02:80"), port)


    def connectedToBluetooth(self):
        self.toolbar.title = 'Done!'
        self.sock.write('4'.encode())
        print("done!")

    def on_press_forward(self):
        self.start_movement()
        print(self.ids)

    def on_release_forward(self):
        self.stop_movement()

    def start_movement(self):
        Clock.schedule_interval(self.move_forward, 0.01)

    def stop_movement(self):
        Clock.unschedule(self.move_forward)

    def move_forward(self, dt):
        print('govno -', self.a)
        if self.a == 'arrow-up-bold-outline':
            self.sock.write('1'.encode())
            sleep(0.01)
            print('1')
        if self.a == 'arrow-down-bold-outline':
            self.sock.write('3'.encode())
            sleep(0.1)
            print('1')

        elif self.a == 'arrow-down-bold-outline':
            self.sock.write('1'.encode())
            print('1')
            sleep(0.1)
            self.sock.write('2'.encode())
            print('2')
            sleep(0.1)


    def returnicon(self, instance):
        self.a = instance.icon
        print(self.a)

class mainapp(MDApp):
    def build(self):
        c = Container()
        return c


if __name__ == '__main__':
    mainapp().run()
