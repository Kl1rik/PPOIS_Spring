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

print("Длина массива аргументов CLI",l)
if l == 1:
    print("Вызов подсказки . Используемые флаги :")
    print("-pay_tel Оплата телефона")
    print("-add_money Внести наличные")
    print("-get_money Снять наличные")
    print("-display_balance Просмотр остатков кард-счета и хранилища банкнот")
elif l > 1:    
    read_flag.flag_reader(l,card_obj)

f.close()