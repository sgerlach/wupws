#!/usr/bin/env bash


python_exe=$(which python2.7)

baseDir="$HOME/wupws"
source "$baseDir/weather.env"
$python_exe "$baseDir/weather_update.py"
