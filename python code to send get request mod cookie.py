import requests


c = {'admin': 'True'}

r = requests.get('https://2019shell1.picoctf.com/flag', cookies=c)
source = r.text
print(source)
