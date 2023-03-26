
import sqlite3
from kivy.lang.builder import Builder
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.textinput import TextInput
Builder.load_file('2lab.kv')
my_path = "C:\\Users\\kiril\\OneDrive\\Документы\\GitHub\\PPOIS_Spring\\Lab 2.2\\PPOIS2lab.db"
connection = sqlite3.connect(my_path)
cursor = connection.cursor()

class TextInput(MDFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def create(self):
        
        return self.screen







class Example(MDApp):
    def build(self):
        title = "Student table"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        data_tables = None
        cursor.execute("SELECT * FROM Students4")
        rows = cursor.fetchall()
        layout = MDFloatLayout()
        button_box = MDBoxLayout(
            pos_hint={"center_x": 0.5},
            adaptive_size=True,
            padding="24dp",
            spacing="24dp",
        )
        for button_text in ["121701", "121702","121703","All","Find Slava"]:
            button_box.add_widget(
                MDRaisedButton(
                    text=button_text, on_release=self.on_button_press
                )
            )
        TextInput(text='Hello world')
        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("No.", dp(10)),
                ("Column 1", dp(20)),
                ("Column 2", dp(20)),
                ("Column 3", dp(20)),
                ("Column 4", dp(20)),
                ("Column 5", dp(20)),
                ("Column 6", dp(20)),
                ("Column 7", dp(20)),
                ("Column 8", dp(20)),
                ("Column 9", dp(20)),
                ("Column 10", dp(20)),
                ("Column 11", dp(20)),
                ("Column 12", dp(20)),
                ("Column 13", dp(20)),
            ],
            row_data=[
                row for row in rows
            ],
        )
        
        
        layout.add_widget(self.data_tables)
        layout.add_widget(button_box)
        return layout
    def on_button_press(self, instance_button: MDRaisedButton) -> None:
        '''Called when a control button is clicked.'''

        try:
            {
                "121701": self.display_121701,
                "121702": self.display_121702,
                "121703":self.display_121703,
                "All":self.display_all,
                "Find":self.find
            }[instance_button.text]()
        except KeyError:
            pass

    def display_121701(self) -> None:
        cursor.execute("SELECT * FROM Students4 Where GroupNumber = 121701")
        rows = cursor.fetchall()
        self.data_tables.update_row_data(self.data_tables,rows)
    def display_121702(self) -> None:
        cursor.execute("SELECT * FROM Students4 Where GroupNumber = 121702")
        rows = cursor.fetchall()
        self.data_tables.update_row_data(self.data_tables,rows)    
    def display_121703(self) -> None:    
        cursor.execute("SELECT * FROM Students4 Where GroupNumber = 121703")
        rows = cursor.fetchall()
        self.data_tables.update_row_data(self.data_tables,rows)  
    def display_all(self) -> None:    
        cursor.execute("SELECT * FROM Students4 ")
        rows = cursor.fetchall()
        self.data_tables.update_row_data(self.data_tables,rows)     
    def find(self) -> None:    
        cursor.execute("SELECT * FROM Students4 Where FullName = 'Find Slava'")
        rows = cursor.fetchall()
        self.data_tables.update_row_data(self.data_tables,rows)        
    
Example().run()
