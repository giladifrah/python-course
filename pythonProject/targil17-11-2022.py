import argparse
import os
import urllib.request

import requests
import sys


from argparse import ArgumentParser

parser = argparse.ArgumentParser()
parser.add_argument('filename', help=' the file to write ')
parser.add_argument('--format', default='html', help=' JSON or HTML, HTML is default ')
parser.add_argument('--url', default='http://www.ynet.co.il', help=' Enter URL ')
args = parser.parse_args()


file = open(args.filename, 'w')
res = requests.get(args.url)

if args.format == 'html':
    file.write(str(res.content))
    #print(res.content)
else:
    file.write(res.json())
