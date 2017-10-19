import urllib2
import re
import urllib

#connect to a URL
course = "gre"
url = "https://"+course+".magoosh.com/lessons"
website = urllib2.urlopen(url)

#read html code
html = website.read()

#use re.findall to get all the links
links = re.findall('\/lessons\/.*', html)
#print links;
for i in links:
	url = i[:-2];
	name =  url.split("/lessons/")[1];
	print name;	
	url =  "https://"+course+".magoosh.com"+url;
	website = urllib2.urlopen(url)
	html = website.read()
	#link = re.findall('https:.*.cloudfront.net.audio_video.*-video-.*.web.mp4', html)
	link = re.findall('<li.* class=.current.*\n<a.*\n<span.*', html)
	#print link;
	link = re.findall('https.*.web',link[0])
	link = link[0]+".mp4";
	print link;
	test=urllib.URLopener()
	test.retrieve(link,name+".mp4");
