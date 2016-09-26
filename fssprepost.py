#!/usr/bin/python
#coding: utf8
import urllib2
import pycurl
from StringIO import StringIO
from lxml import etree
def main():
    rss_url='http://r09.fssprus.ru/news/rss'
    #response = urllib2.urlopen(rss_url)
    #html = response.read()
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, rss_url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue()
    #print(body)
    xml=etree.fromstring(body)
    chan= xml.find('channel')
    items=chan.findall('item')
    print len(items)
    title= items[0].find('title').text
    description= items[0].find('description').text
    pubDate= items[0].find('pubDate').text
    #titlecdata=title.find('CDATA')
    print (title)
    print description
    print pubDate
if __name__ == "__main__":
    main()
