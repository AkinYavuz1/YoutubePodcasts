from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = "https://www.youtube.com/results?search_query=podcast&sp=CAM%253D"

#open the connection, read the page
open_url = uReq(url)
page_html = open_url.read()

#close the connection
open_url.close()

#html parsing
page_soup = soup(page_html, "html.parser")

find_videos = page_soup.findAll("div", {"class" : "text-wrapper style-scope ytd-video-renderer"})

print(page_soup.body.a)

#print(find_videos)
