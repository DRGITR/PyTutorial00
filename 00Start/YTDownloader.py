# importing pytube library

# pip install pytube

import pytube

url = input("Paste the URL: ")

path = "/Users/tusharmahore/Downloads" # path = "C:"

# Actual line of Code to download video
pytube.YouTube(url).streams.get_highest_resolution().download(path)
