import requests
import sqlite3
import datetime


def conectarBD(response):
	conexion = sqlite3.connect('enviame.db')
	cursor = conexion.cursor()
	date = datetime.datetime.now()

	cursor.execute("CREATE TABLE IF NOT EXISTS enviame_api (id INTEGER PRIMARY KEY AUTOINCREMENT,response VARCHAR(100), created TEXT)")
	cursor.execute("INSERT INTO enviame_api (id, response, created) VALUES (null, ?, ?)",(response,date,))
	conexion.commit()
	conexion.close()


def enviame():
	url = "https://stage.api.enviame.io/api/s2/v2/companies/401/deliveries"
	payload =  "{\n    \"shipping_order\": {\n        \"n_packages\": \"1\",\n        \"content_description\": \"ORDEN 255826267\",\n        \"imported_id\": \"255826267\",\n        \"order_price\": \"24509.0\",\n        \"weight\": \"0.98\",\n        \"volume\": \"1.0\",\n        \"type\": \"delivery\"\n    },\n    \"shipping_origin\": {\n        \"warehouse_code\": \"401\"\n    },\n    \"shipping_destination\": {\n        \"customer\": {\n            \"name\": \"Bernardita Tapia Riquelme\",\n            \"email\": \"b.tapia@outlook.com\",\n            \"phone\": \"977623070\"\n        },\n        \"delivery_address\": {\n            \"home_address\": {\n                \"place\": \"Puente Alto\",\n                \"full_address\": \"SAN HUGO 01324, Puente Alto, Puente Alto\"\n            }\n        }\n    },\n    \"carrier\": {\n        \"carrier_code\": \"\",\n        \"tracking_number\": \"\"\n    }\n}"
	headers = {
	  'Accept': 'application/json',
	  'api-key': 'ea670047974b650bbcba5dd759baf1ed',
	  'Content-Type': 'application/json'
	}

	response = requests.request("POST", url, headers=headers, data = payload)
	response_text = response.text.encode('utf8')
	print(response_text)
	conectarBD(response_text)

enviame()
