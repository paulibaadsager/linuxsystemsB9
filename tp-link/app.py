import flask
import asyncio
from kasa import SmartPlug
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#ipm="192.168.8.101"
#p = SmartPlug(ipm)

#async def testing():
#    await p.update()
#    return p.alias
##---
async def get_alias(ip):
    p = SmartPlug(ip)
    await p.update()
    return p.alias

async def get_state(ip):
    p = SmartPlug(ip)
    await p.update()
    return p.state_information

async def is_on(ip):
    p = SmartPlug(ip)
    await p.update()
    return p.is_on

async def turn_off(ip):
    p = SmartPlug(ip)
    await p.turn_off()

async def turn_on(ip):
    p = SmartPlug(ip)
    await p.turn_on()

@app.route('/info/<ip>')
def get_info(ip):
    alias=asyncio.run(get_alias(ip))
    powerStatus=asyncio.run(is_on(ip))
    return flask.jsonify({
        'ip': ip,
        'alias': alias,
        'Power on': powerStatus
        })

@app.route('/alias/<ip>')
def alias(ip):
    res=asyncio.run(get_alias(ip))
    return flask.jsonify({'alias': res})

@app.route('/state/<ip>')
def status(ip):
    res=asyncio.run(get_state(ip))
    return flask.jsonify(res)

@app.route('/powerstatus/<ip>')
def powerstatus(ip):
    res=asyncio.run(is_on(ip))
    return flask.jsonify({'Power on': res})

@app.route('/deactivate/<ip>', methods=['POST'])
def turnoff(ip):
    asyncio.run(turn_off(ip))
    return flask.jsonify({'msg':'Device asked to turn off'})

@app.route('/activate/<ip>', methods=['POST'])
def turnon(ip):
    asyncio.run(turn_on(ip))
    return flask.jsonify({'msg':'Device asked to turn on'})

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
