import requests

text = requests.get('https://news.baidu.com')
print(text.headers)