#!/usr/bin/python
#
# Display system status and hashrate from FlyPool miner
#
# Based on tutorial: https://www.rototron.info/lcd-display-tutorial-for-raspberry-pi/
from flypool.miner import Miner
from Adafruit_CharLCD import Adafruit_CharLCD
import time

import conf

# Specify pins for LCD
lcd = Adafruit_CharLCD(rs=26, en=19,
                       d4=13, d5=6, d6=5, d7=11,
                       cols=16, lines=2)
# Clear the LCD Screen
lcd.clear()

# Script Settings
api = 'fly-pool'
miner = conf.miner

# Run infinite loop
while True:
    # Make Request
    request = Miner(api, miner)
    status = request.status()

    # Check if system is online
    if status['activeWorkers'] > 0:
        system_status = 'System Online'
    else:
        system_status = 'System Offline'

    # Format hashrate
    hashrate = round(status['currentHashrate'], 2)

    if hashrate > 999:
        hashrate = str(round(hashrate / 1000, 2))
        hashrate_suffix = ' KH/s'
    else:
        hashrate = str(round(hashrate, 0))
        hashrate_suffix = ' H/s'

    # Display system information
    lcd.message(system_status + '\n' + 'Rate: ' + hashrate + hashrate_suffix + ' ')

    # Sleep for 10 minutes to prevent hammering endpoint
    time.sleep(120)
