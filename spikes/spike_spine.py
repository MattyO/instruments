import spyne
from spyne.protocol.json import JsonDocument, JsonRpc
from spyne.protocol.http import HttpRpc
from spyne.server.wsgi import WsgiApplication
from spyne.model.primitive import String

class HelloWorldService(spyne.ServiceBase):
    @spyne.srpc(spyne.AnyDict)
    def position_changed(position_data):
        print 'things are happening'
        print got_some_data
        return {"a_key":"a_value"}

application = spyne.Application([HelloWorldService],
    tns='spyne.examples.hello',
    in_protocol=HttpRpc(validator='soft'),
    out_protocol=JsonDocument()
)

if __name__ == '__main__':
    print 'starting server'
    # You can use any Wsgi server. Here, we chose
    # Python's built-in wsgi server but you're not
    # supposed to use it in production.
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 9000, wsgi_app)
    server.serve_forever()
