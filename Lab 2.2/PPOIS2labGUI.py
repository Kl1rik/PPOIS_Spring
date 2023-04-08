
import sqlite3
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
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager


class WindowManager(MDScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)


class FirstWindow(MDScreen):
    pass
    
    
        
class SecondWindow(MDScreen):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        self.get_students()
    def get_students(self):
        my_path = "C:\\Users\\kiril\\OneDrive\\Документы\\GitHub\\PPOIS_Spring\\Lab 2.2\\PPOIS2lab.db"
        connection = sqlite3.connect(my_path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Students4")
        rows = cursor.fetchall()
        
        self.data_items = [row for row in rows]

    
    

class ThirdWindow(MDScreen):
   pass
        
    
   




class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        Builder.load_file('main.kv')
        


        screen_manager = WindowManager()
        screen_manager.add_widget(FirstWindow(name = "main"))
        screen_manager.add_widget(SecondWindow(name = "all"))
        screen_manager.add_widget(ThirdWindow(name = "find"))
        return screen_manager
    
Example().run()



















# row_data: [self.data_items]


# MDTextField:
#                 id: last_name
#                 mode: "rectangle"
#                 hint_text: "Фамилия студента"
#                 max_text_length: 100
#                 required: True
#                 multiline: False
#                 on_text: root.filter()
#             MDTextField:
#                 id: group_number
#                 mode: "rectangle"
#                 hint_text: "Номер группы студента"
#                 max_text_length: 10
#                 multiline: False
#                 on_text: root.filter()
#             MDRectangleFlatButton:
#                 id: hours_choose
#                 text: 'Выберите тип пропуска'
#                 on_release: root.hours_dropdown()
#                 pos_hint: {'center_x': .5, 'center_y': .5}
#             MDTextField:
#                 id: lower_hours_limit
#                 mode: "rectangle"
#                 hint_text: "Нижний предел"
#                 input_filter: "int"
#                 multiline: False
#                 on_text: root.filter()
#             MDTextField:
#                 id: upper_hours_limit
#                 mode: "rectangle"
#                 hint_text: "Верхний предел"
#                 input_filter: "int"
#                 multiline: False
#                 on_text: root.filter()
        