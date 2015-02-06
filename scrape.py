"""
Dependencies
sudo apt-get install libxml2-dev libxslt-dev python-dev lib32z1-dev
"""

from lxml import html
import requests
import numpy as np

def getLink():
	"""
	extracts link from allLink file
	"""
	newRow = []
	with open("allLinks.txt") as myFile:
		for link in myFile:
			newRow += getHTML(link.strip())

	with open("allData.txt", "w+") as myFile:
		for row in newRow:
			myFile.write(row)

def getHTML(link=None):
	"""
	Some doc string
	"""
	#link = "https://play.google.com/store/apps/details?id=com.sticksports.stickcricket"
	#link = "https://play.google.com/store/apps/details?id=air.com.mobestmedia.roomescape100"
	page = requests.get(link)
	tree = html.fromstring(page.text)
	gameName = tree.xpath('//*[@id="body-content"]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/text()')
	rating = tree.xpath('//div[@class="score"]/text()')
	ratingBreakup = [int(count.replace(',','')) for count in tree.xpath('//span[@class="bar-number"]/text()')]
	print link
	print unicode(gameName)
	print rating
	print ratingBreakup
	fulldata = gameName[0].encode('utf-8')+";"+rating[0]+";"
	for score in ratingBreakup:
		fulldata += str(score)+";"
	fulldata += link+"\n"
	return fulldata


getLink()
#getHTML()