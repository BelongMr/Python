# -*- coding:utf-8 -*-
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

#begin bookHandler
class bookHandler(ContentHandler):
    inAuthor = False
    inTitle = False
    def startElement(self, name, attrs):
        if name == "book":
            print("****Book*****")
        if name == "title":
            self.inTitle = True
            print("Title:",)
        if name == "author":
            self.inAuthor = True
            print("Author:",)
    def endElement(self,name):
        if name == "title":
            self.inTitle = False
            print("Title:",)
        if name == "author":
            self.inAuthor = False
            print("Author:",)

    def characters(self, content):
        if self.inTitle or self.inAuthor:
            print(content)

#end bookHandler

parser = make_parser()
parser.setContentHandler(bookHandler())
parser.parse("library.xml")
