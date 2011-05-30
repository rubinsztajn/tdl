import os
import sys
import urllib2
from lxml import etree

ns = {
      'rdf' : 'http://www.w3.org/1999/02/22-rdf-syntax-ns#', 
      'fedora-model' : 'info:fedora/fedora-system:def/model#'
     }

base_url = "http://repository01.lib.tufts.edu:8080/fedora/objects/%s/datastreams"

def read_url(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    return response.read()

def load(pid):
    do_url = base_url % (pid)

    rdf = read_url(do_url + '/RELS-EXT/content')
    rels = etree.fromstring(rdf)
    hasModel = rels.xpath('//fedora-model:hasModel', namespaces=ns)
    resource = "{%s}resource" % (ns['rdf'])
    content_model = hasModel[0].attrib[resource][15:]

    if content_model == 'Image.4DS':
       return Image4DS(do_url)

    elif content_model == 'Text.FacPub':
        return TextFacPub(do_url)

class Datastream:
    def __init__(self, url):
        self.url = url
        
    def download(self, filename):
        out = open(filename, 'w')

        out.write(read_url(self.url))
        
class Image4DS:
    def __init__(self, do_url):
        
        self.dc = Datastream(do_url + '/DC/content')
        self.archival = Datastream(do_url + '/Archival.tif/content')
        self.advanced = Datastream(do_url + '/Advanced.jpg/content')
        self.basic = Datastream(do_url + '/Basic.jpg/content')
        self.thumb = Datastream(do_url + '/Thumbnail.png/content')

class TextFacPub:
    def __init__(self, do_url):
        
        self.dc = Datastream(do_url + '/DC/content')
        self.pdf = Datastream(do_url + '/Archival.pdf/content')
        self.access_xml = Datastream(do_url + '/Access.xml/content')

class TextPDF:
    def __init__(self, do_url):

        self.dc = Datastream(do_url + '/DC/content')
        self.pdf = Datastream(do_url + '/Archival.pdf/content')
        self.access_xml = Datastream(do_url + '/Access.xml/content')

class Audio:
    def __init__(self, do_url):

        self.dc = Datastream(do_url + '/DC/content')
        self.access = Datastream(do_url + '/ACCESS_MP3/content')
        self.archival = Datastream(do_url + '/ARCHIVAL_AUDIO/content')

class TextTEI:
    def __init__(self, do_url):

        self.dc = Datastream(do_url + '/DC/content')
        self.access = Datastream(do_url + '/Access.xml/content')
        self.archival = Datastream(do_url + '/Archival.xml/content')


        
