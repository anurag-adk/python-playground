# import urllib.request, json

# url=input('Enter url: ')
# html=urllib.request.urlopen(url).read().decode()
# data=json.loads(html)
# count=0

# for comment in data['comments']:
#     count+=int(comment['count'])

# print(f"The count is: {count}")

# # https://py4e-data.dr-chuck.net/comments_1758613.json

import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter - ')
uh = urllib.request.urlopen(url)
data = uh.read().decode()

info = json.loads(data)

# print(data)

for item in info['comments']:
  print(item['count'])