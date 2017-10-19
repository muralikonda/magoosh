import urllib2
import re
import urllib

#connect to a URL
course = "gmat"
url = "https://"+course+".magoosh.com/lessons"
website = urllib2.urlopen(url)

#read html code
html = website.read()

#use re.findall to get all the links
links = re.findall('\/lessons\/.*"><', html)
#print links;
for i in links:
	url = i[:-3];
	name =  url.split("/lessons/")[1];
	url =  "https://"+course+".magoosh.com"+url;
	print url;
	website = urllib.urlopen(url)
	#print urllib.urlopen(url).read()
	#print website," website";	
	html = website.read()
	#link = re.findall('https:.*.cloudfront.net.audio_video.*-video-.*.web.mp4', html)
	#link = re.findall('<div.* class=.current.*\n<a.*\n<span.*', html)
	link = re.findall('<div.*.current".*.div>', html)
	link = re.findall('https.*.web',link[0])
	link = link[0]+".mp4";
	test=urllib.URLopener()
	test.retrieve(link,name+".mp4");
