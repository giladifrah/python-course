import os
import requests
import sys

from argparse import ArgumentParser


parser = ArgumentParser(description='Get the current weather information')
parser.add_argument('zip', help='zip/postal code to get weather for')
parser.add_argument('--country', default='us', help='country zip/postal belongs to ')

args = parser.parse_args()


api_key = os.getenv('OWN_API_KEY')

if not api_key:
    print("ERROR: No 'OWN_API_KEY' Provided")
    sys.exit(1)


url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"

res = requests.get(url)

if res.status_code != 200:
    print(f"ERROR Talking to weather provider : {res.status_code}")
    sys.exit(1)

print(res.json())