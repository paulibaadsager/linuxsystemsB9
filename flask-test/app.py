import flask
import asyncio
from kasa import SmartPlug
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

p = SmartPlug("192.168.8.101")
async def main():

    await p.update()
    #print(p.alias)
    return p.alias

async def mainto():
    await p.turn_off()


@app.route('/status')
def status():
    res=asyncio.run(main())
    return flask.jsonify({'alias': res})


@app.route('/deactivate', methods=['POST'])
def turnoff():
    asyncio.run(mainto())
    return flask.jsonify({'msg':'slukket'})


@app.route('/navn', methods=['POST'])
def hurra():
    print(request.get_json())
    return flask.jsonify({'Du hedder:': 6})


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
