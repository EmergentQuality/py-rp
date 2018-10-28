#! usr/bin/python3
import requests

with open('dark_sky_sample.json', mode='r') as jfile:

    print(jfile['currently']['summary'])
