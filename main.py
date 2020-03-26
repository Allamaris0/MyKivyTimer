from kivy.app import App
from kivy.uix.widget import Widget
from datetime import *
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout

class CenterBox(Widget):
    con = ObjectProperty(None)
    now = datetime.now()
    start = timedelta(hours=0, minutes=0, seconds=0)
    trigger = 0
    store = None
    sound = SoundLoader.load('bell.mp3')

    numberlist=[t for t in range(0,60)] #Variable to Set Alarm Popop

    def update_clock(self, *args):
        self.now = datetime.now()
        self.label1.text = self.now.strftime('%H:%M:%S')

        if self.store!=None:
            try:
                store_hour=datetime(self.now.year, self.now.month, self.now.day, int(self.store[0]), int(self.store[1]), int(self.store[2]))
                if datetime.timestamp(store_hour) <= datetime.timestamp(self.now):
                    self.sound.play()
                    self.store=None

            except:
                exceptPopup=Popup(title="Alarm Clock", content=Label(text='Invalid value', font_size= '20sp'), size_hint=(0.5, 0.5))
                exceptPopup.open()
                self.store=None

        if self.trigger==1:
            self.start = self.start + timedelta(seconds=1)
            self.label2.text = str(self.start)
            self.btn_start.text = 'Reset'

        elif self.trigger>=1:
            self.label2.text="0:00:00"
            self.start = timedelta(hours=0, minutes=0, seconds=0)
            self.trigger=1

    def openpop(self):
        self.con = PopAlarm()
        self.con.title='Set Alarm Clock'
        self.con.size_hint=(0.7,0.7)
        self.con.content = PopContent()
        self.con.open()

    def add(self,attribute,input_value):
        #The function to Set Alarm Popup
        try:
            input_value=int(input_value)
            if attribute=="hour":
               if input_value>=23:
                   input_value = 0
               else:
                   input_value = self.numberlist[self.numberlist.index(input_value) + 1]
            elif attribute=="min":
               if input_value>=59:
                   input_value = 0
               else:
                   input_value = self.numberlist[self.numberlist.index(input_value) + 1]
            elif attribute=="sec":
               if input_value>=59:
                   input_value = 0
               else:
                   input_value= self.numberlist[self.numberlist.index(input_value) + 1]
            return input_value
        except:
            input_value=0
            return input_value

    def subtract(self,attribute,input_value):
        # The function to Set Alarm Popup
        try:
            input_value=int(input_value)
            if attribute=="hour":
               if input_value<=0:
                   input_value = 23
               else:
                   input_value = self.numberlist[self.numberlist.index(input_value) - 1]
            elif attribute=="min":
               if input_value<=0:
                   input_value = 59
               else:
                   input_value = self.numberlist[self.numberlist.index(input_value) - 1]
            elif attribute=="sec":
               if input_value<=0:
                   input_value = 59
               else:
                   input_value = self.numberlist[self.numberlist.index(input_value) - 1]
            return input_value
        except:
            input_value=0
            return input_value





class PopAlarm(Popup):
    def closeme(self):
        self.dismiss()

class PopContent(GridLayout):
    pass


class MyKivyTimerApp(App):
    def build(self):
        layout=CenterBox()
        Clock.schedule_interval(layout.update_clock, 1)
        return layout


if __name__== "__main__":
    MyKivyTimerApp().run()

