from wyze_sdk import Client
from wyze_sdk.errors import WyzeApiError
import config

email = config.email
password = config.password

client = Client(config.email, config.password)

def list_devices():
	try:
		response = client.devices_list()
		for device in response:
			print(f'mac: {device.mac}')
			print(f'nickname: {device.nickname}')
			print(f'is online: {device.is_online}')
			print(f'is on: {device.is_on}')
			print(f'product model: {device.product.model}')
	except WyzeApiError as e:
		print(f'error: {e}')

def bulb_switch():
	try:
		bulb = client.bulbs.info(device_mac=config.lamp2_mac)
		print(f"power: {bulb.is_on}")
		print(f"online: {bulb.is_online}")

		if bulb.is_on:
			client.bulbs.turn_off(device_mac=bulb.mac, device_model=bulb.product.model)
		else:
			client.bulbs.turn_on(device_mac=bulb.mac, device_model=bulb.product.model)

			bulb = client.bulbs.info(device_mac=bulb.mac)
			assert bulb.is_on is True
	except WyzeApiError as e:
		print(f"error: {e}")

def set_device_properties():
	try:
		bulb = client.bulbs.info(device_mac=config.lamp2_mac)
		print(f"power: {bulb.is_on}")
		print(f"online: {bulb.is_online}")
		print(f"brightness: {bulb.brightness}")
		print(f"temp: {bulb.color_temp}")
		print(f"color: {bulb.color}")

		client.bulbs.set_brightness(device_mac=bulb.mac, device_model=bulb.product.model, brightness=50)
		client.bulbs.set_color(device_mac=bulb.mac, device_model=bulb.product.model, color='ff00ff')
		client.bulbs.set_color_temp(device_mac=bulb.mac, device_model=bulb.product.model, color_temp=3800)
		
		# bulb = client.bulbs.info(device_mac=config.lamp2_mac)
		# assert bulb.brightness == 100
		# assert bulb.color == 'ff00ff'
		# assert bulb.color_temp == 3800

		client.bulbs.set_away_mode(device_mac=bulb.mac, device_model=bulb.product.model, away_mode=True)
	
	except WyzeApiError as e:
		print(f"error: {e}")


help(client)