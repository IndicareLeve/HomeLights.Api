from flask import Flask, request, render_template
from yeelight import Bulb
# import time
# import sys
# import RPi.GPIO as GPIO
# import Adafruit_WS2801
# import Adafruit_GPIO.SPI as SPI

# PIXEL_COUNT = 96
# SPI_PORT = 0
# SPI_DEVICE = 0
# pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)
bulb = Bulb("192.168.1.7")
app = Flask(__name__)


@app.route('/Lights/On', methods=['PUT'])
def lightson():
    bulb.turn_on()

    return ('', 204)


@app.route('/Lights/Off', methods=['PUT'])
def lightsoff():
    bulb.turn_off()

    return ('', 204)


@app.route('/Lights/Color', methods=['PUT'])
def lightscolor():
    data = request.get_json()
    bulb.set_rgb(data['r'], data['g'], data['b'])

    return ('', 204)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
