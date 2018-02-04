from subprocess import call
from subprocess import check_output
import subprocess
import re

def get_station_names():
    string = check_output(['mpc', 'playlist']).decode('utf-8')
    cleanlist = list(filter(None, string.split("\n")))
    return cleanlist


