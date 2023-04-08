import sqlite3
import sys
from kivy.lang.builder import Builder
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivy.lang.builder import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivymd.uix.datatables.datatables import MDDataTable
from kivymd.uix.menu.menu import MDDropdownMenu
from kivy.clock import Clock
from typing import Optional
from kivymd.uix.screenmanager import MDScreenManager
from PPOIS1lab import Rewrite_values,Get_money,Add_money,Pay_telephone,Read_values,Display_values,Flag_Reader
from PPOIS1labClasses import Atm,Card,Bank,Telephone
f = open("C:\\Users\\kyrill\\Downloads\\Telegram Desktop\\PPOIS1lab.txt","r+")
l = len(sys.argv)
read_flag = Flag_Reader()
display = Display_values()
get = Get_money()
add = Add_money()
pay = Pay_telephone()
rewrite = Rewrite_values()
read = Read_values()
arr =read.read_values()
atm = arr[0]
bank = arr[1]
pin = arr[2]
card = arr[3]
tel = arr[4]
atm_obj = Atm(atm)
card_obj = Card(pin,card)
bank_obj = Bank(bank)
tel_obj = Telephone(tel)

class WindowManager(MDScreenManager):
    def __init__(self, *args, **kwargs):
        super(WindowManager,self).__init__(*args, **kwargs)

class MenuScreen(MDScreen):
    pass
class AddMoneyScreen(MDScreen):
    pass
class GetMoneyScreen(MDScreen):
    pass
class PayTelephoneScreen(MDScreen):
    pass
class DisplayScreen(MDScreen):
    pass
class ValidateScreen(MDScreen):
    pass
class AtmApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        Builder.load_file('Gui4lab.kv')
        screen_manager = WindowManager()
        screen_manager.add_widget(MenuScreen(name = "menu"))
        screen_manager.add_widget(AddMoneyScreen(name = "add"))
        screen_manager.add_widget(GetMoneyScreen(name = "get"))
        screen_manager.add_widget(DisplayScreen(name = "display"))
        screen_manager.add_widget(PayTelephoneScreen(name = "pay"))
        screen_manager.add_widget(ValidateScreen(name = "validate"))


        return screen_manager
    
AtmApp.run()
f.close()