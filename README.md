# FlyPool Monitor 16x2 Display Raspberry Pi
- **16x2 LCD Display Setup:** https://www.rototron.info/lcd-display-tutorial-for-raspberry-pi/
![Pinout](https://www.rototron.info/wp-content/uploads/LCD-Display01.png)

## Setup
- Install Python 3.6 on Raspbian: https://gist.github.com/dschep/24aa61672a2092246eaca2824400d37f
- Install dependencies:
  - `sudo pip3.6 install requests`
  - `sudo pip3.6 install adafruit-charlcd`
- Run setup script to generate conf.py file.  This file will include your public miner address.
  - `./setup.sh`

## Basic Usage
- **Enable 16x2 Display on Raspberry Pi**
  - `python3.6 monitor.py`
 
## Demo
![16x2 LCD Flypool Miner Display](https://i.imgur.com/kGTmJBV.jpg)
