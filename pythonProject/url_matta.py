import requests
# import sys

from argparse import ArgumentParser

parser = ArgumentParser('Get html or json from url')
parser.add_argument('url',help='Must enter url')
parser.add_argument('destination',help='Must enter destination')
parser.add_argument('--state',default='html',help='CHOOSE html OR json as values, by default html')
args = parser.parse_args()
res = requests.get(args.url)

if args.state == 'html':
    filecontent = res.content
    finalfilename = args.destination.replace('.json','.html')
else:
    # filecontent =  res.json()
    filecontent = res.text
    finalfilename = args.destination.replace('.html', '.json')

with open(finalfilename, 'a') as f:
    f.write(str(filecontent))
    f.close()