#!/bin/bash

sudo apt-get install python3-pip xclip -y

mkdir -p ~/src && git clone git@github.com:flads/tfaker.git ~/src/tfaker

cd ~/src/tfaker && pip3 install -r requirements.txt

sudo ln -s ~/src/tfaker/tfaker.py /usr/local/bin/tf
