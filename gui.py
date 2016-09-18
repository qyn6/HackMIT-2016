__version__ = '1.9'
import midi
import arduinoserial
from time import sleep


from kivy.app import App
import numpy as np
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
import os






class GrandParent(GridLayout):
	def __init__(self,**kwargs):
		super(GrandParent, self).__init__(**kwargs)

		self.song = None
	def start(self):
		print self.song

		

		pattern = midi.read_midifile(self.song+".mid")
		count = 0
		notes = []
		for track in pattern:
		    for event in track:

		        if isinstance(event, midi.NoteOnEvent):
		            notes.append((event.data[0], event.tick))
		            #print type(event)
		            #print event.tick
		            count += 1
		            #print count

		arduino = arduinoserial.SerialPort('/dev/cu.usbmodem1411',9600)
		for (note,time) in notes:
			sleep(2)
			arduino.write_byte(note)
			# print str(note)
			# print arduino.read_until('\n')



class GuiApp(App):
    def build(self):


        layout = GrandParent()
        #layout.add_widget(Picture())

        
        return layout

if __name__ == '__main__':
    GuiApp().run()