from xml.dom.minidom import parse
import urllib
import xml.etree.ElementTree as ET

xmlurl = 'http://ws.spotify.com/lookup/1/?uri=spotify:track:'

def parseTrack(xmlpath):
	xml = urllib.urlopen(xmlpath)
	dom = parse(xml)
	names = dom.getElementsByTagName('name')
	songName = names[0].firstChild.data
	artistName = names[1].firstChild.data
	return artistName
	
def getURIs(file):
	uris = []
	lines = [line.strip() for line in open('raw.txt')]
	for line in lines:
		uri = line[30:]
		if len(uri) == 22:
			uris.append(uri)
	return uris

tree = ET.parse(urllib.urlopen(xmlurl+'1XKopm6Ka62xxgI3xIjcRJ'))
root = tree.getroot()

for child in root:
	print child.tag