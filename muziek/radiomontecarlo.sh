#!/bin/bash
timeout 10800 wget -O - https://icy.unitedradio.it/RMC.mp3 | madplay - --no-tty-control
