from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
#C:\Users\FireFist\Desktop\hax.py

class Xyz(App):
	def build(self):
		f = FloatLayout()
		l = Label(text="YO",font_size = 100)
		f.add_widget(l)
		return f

if __name__ =="__main__":
	Xyz().run()

#print('NEW')
