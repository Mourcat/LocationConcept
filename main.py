import kivy
kivy.require('2.1.0')
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from screens import MainScreen, InScreen


class LocationDefinerApp(MDApp):
	title = "I'll find your location".upper()
	
	def build(self):
		self.theme_cls = ThemeManager()
		self.theme_cls.theme_style = 'Dark'
		self.theme_cls.primary_palette = 'LightGreen'
		self.theme_cls.accent_palette = 'BlueGray'
		self.root = MainScreen()
		return self.root

	def on_start(self):
		self.root.ids.sm.current = 'inscreen'
	
		
if __name__ == '__main__':
	LocationDefinerApp().run()