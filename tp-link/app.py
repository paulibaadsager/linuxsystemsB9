import flask
import asyncio
from kasa import SmartPlug
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

ip="192.168.8.101"
p = SmartPlug(ip)

#async def testing():
#    await p.update()
#    return p.alias
##---
async def get_alias():
    await p.update()
    return p.alias

async def get_state():
    await p.update()
    return p.state_information

async def is_on():
    await p.update()
    return p.is_on

async def turn_off():
    await p.turn_off()

async def turn_on():
    await p.turn_on()

@app.route('/info')
def get_info():
    alias=asyncio.run(get_alias())
    powerStatus=asyncio.run(is_on())
    return flask.jsonify({
        'ip': ip,
        'alias': alias,
        'Power ON': powerStatus
        })

@app.route('/alias')
def alias():
    res=asyncio.run(get_alias())
    return flask.jsonify({'alias': res})

@app.route('/state')
def status():
    res=asyncio.run(get_state())
    return flask.jsonify(res)

@app.route('/powerstatus')
def powerstatus():
    res=asyncio.run(is_on())
    return flask.jsonify({'Power ON': res})

@app.route('/deactivate', methods=['POST'])
def turnoff():
    asyncio.run(turn_off())
    return flask.jsonify({'msg':'Device asked to turn off'})

@app.route('/activate', methods=['POST'])
def turnon():
    asyncio.run(turn_on())
    return flask.jsonify({'msg':'Device asked to turn on'})


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
