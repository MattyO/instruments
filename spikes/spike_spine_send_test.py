from spyne.client.http import HttpClient
from rpc import application

client = HttpClient("http://0.0.0.0:9000", application)
client.service.position_changed()
