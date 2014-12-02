import gps
from pprint import pprint
import bjsonrpc
 
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
client = None
try:
    client = bjsonrpc.connect(host="10.0.0.22", port=9001)
except Exception as ex:
    print 'exception happening{}'.format(ex)

 
while True:
    report = session.next()
    if report['class'] == 'TPV':
        response = client.call.change_position(dict(report))
