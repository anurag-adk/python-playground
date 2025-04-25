# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter URL: ')
# position = int(input('Enter position: '))
# repeat = int(input('Enter repeat: '))

# for _ in range(repeat):
#     html = urllib.request.urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')
    
#     # Retrieve all of the anchor tags
#     tags = soup('a')
    
#     # position ko lagi
#     if position <= len(tags):
#         url = tags[position - 1].get('href')
#         print("Last URL:", url)

# https://py4e-data.dr-chuck.net/known_by_Meryl.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count:'))
position = int (input('Enter position:'))

for _ in range(count):
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all of the anchor tags
        tags = soup('a')
        for x in range(position):
                url = tags[x].get('href')
        print(url)