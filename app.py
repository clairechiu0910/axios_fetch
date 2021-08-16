from flask import Flask, render_template, request, jsonify
from packages.model import Model

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def call_api():
    json_data = request.get_json()
    sec = json_data['sec']
    
    Model(sec=sec).call()
    
    res = {'data': 'call api success'}    
    return jsonify(res)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port='5000') // 可以用server的ip直接call這個網站 (http://140.114.76.xxx:5000)
    app.run()