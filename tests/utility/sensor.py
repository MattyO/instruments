from flask import Flask, render_template, redirect, url_for, request
import bjsonrpc

app = Flask(__name__)
app.debug = True
test_data = {"heading":1}
qtapp = bjsonrpc.connect(host='0.0.0.0', port=9001)

@app.route("/", methods=['get'])
def index():
    return render_template('index.html')

@app.route("/", methods=['post'])
def send_info():
    test_data.update(request.form)
    print test_data
    for key, value in test_data.items():
        test_data[key] = float(value[0])
    qtapp.call.change_position(test_data)
    return redirect('/')

if __name__ =="__main__":
    app.run()
