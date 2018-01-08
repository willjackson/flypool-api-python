#!/bin/bash

# Get public key
echo "What is your miner public key?"
read public_key

#  Create or update settings file
if [ ! -f ./conf.py ]; then
    cp ./conf.py.example ./conf.py
  else
    rm -rf ./conf.py
    cp ./conf.py.example ./conf.py
fi

# Write public key to settings file
sed -i -e "s/YOUR_MINER_PUBLIC_KEY/$public_key/g" ./conf.py