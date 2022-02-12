import webbrowser
import os
import random

files = [f for f in os.listdir('.') if os.path.isfile(f)]

links = []

for f in files:
  if f[-4:] == '.url':
    read = open(f, "r")
    links.append(read.read().split('URL=')[1].split('\n')[0])

webbrowser.open(links[random.randint(0, len(links)-1)])