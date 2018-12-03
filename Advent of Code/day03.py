import urllib.request

uf = urllib.request.urlopen('https://pastebin.com/raw/B0mXqMEX')
html = uf.readlines()

lines = [line.decode('utf-8').strip('\r\n') for line in html]

# for line in html:
#     print(line)
# print(html)