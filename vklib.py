#!/usr/bin/python
#coding: utf8
import urllib2
import pycurl
from StringIO import StringIO
from lxml import etree
from urllib  import urlencode
import json
vkurl="https://oauth.vk.com"
vkurl2="https://api.vk.com/method"
def getvktoken():
    f=file('./config.xml')
    xml=etree.parse(f)
    root=xml.getroot()
    vk=root.find('vk')
    data=vk.attrib
    data['v']='5.53'
    data['grant_type']='client_credentials'
    buffer = StringIO()
    c = pycurl.Curl()
    enc_data= urlencode(data)
    req_url=vkurl +'/'+'access_token'+'/' "?" + enc_data
    #print req_url
    c.setopt(c.URL, req_url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue()
    tok=json.loads(body)['access_token']
    #print tok
    return tok
def getinfo(tok):
    data={}
    data['access_token']=tok
    data['v']='5.53'
    #data['grant_type']='client_credentials'
    buffer = StringIO()
    c = pycurl.Curl()
    enc_data= urlencode(data)
    req_url=vkurl2 +'/'+'account.getProfileInfo'+'/' "?" + enc_data
    print req_url
    c.setopt(c.URL, req_url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue()
    print body
def main():
    #f=file('./config.xml')
    #xml=etree.parse(f)
    #root=xml.getroot()
    #vk=root.find('vk')
    #data=vk.attrib 
    #print body
    #tok=getvktoken()
    #print tok
    getinfo(getvktoken())
if __name__ == "__main__":
    main()
