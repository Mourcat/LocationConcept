from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivymd.uix.screen import MDScreen
from kivy_garden.mapview import MapView, MapMarker
import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode, OpenCageGeocodeError


Builder.load_file('screens/InScreen/InScreen.kv')


API_KEY = '40a0f498d12241618d9cb4755f188846'


class InScreen(MDScreen):
	phone_number = StringProperty()
	dialog = None
	phone_data = dict()
	map = ObjectProperty()

	def map_opacity_control(self, instance):
		print(4*instance.opacity)
		self.map.zoom = int(4+4*instance.opacity)


	def data_reciever(self):
		parsed_num = phonenumbers.parse(self.phone_number)
		self.phone_data['country'] = geocoder.description_for_number(parsed_num, 'en')
		self.phone_data['service'] = carrier.name_for_number(parsed_num, 'en')
		try:
			cage_geo = OpenCageGeocode(API_KEY)
			query = str(self.phone_data['country'])
			response = cage_geo.geocode(query)
		except OpenCageGeocodeError:
			print('Something wrong')
		self.phone_data['lat'] = response[0]['geometry']['lat']
		self.phone_data['lng'] = response[0]['geometry']['lng']
		self.ids.geo_lbl.text = f"{self.phone_data['country']} {self.phone_data['service']}\n" \
								f"{self.phone_data['lat']} {self.phone_data['lng']}"
		self.map = MapView(zoom=2, lat=self.phone_data['lat'], lon=self.phone_data['lng'])
		self.ids.map.add_widget(self.map)

	def btn_toggle(self, instance):
		if instance.text:
			self.ids.define_btn.disabled = False
			self.phone_number = f'+{instance.text}'
		else:
			self.ids.define_btn.disabled = True