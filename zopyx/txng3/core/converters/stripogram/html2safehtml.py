# Copyright (c) 2001 Chris Withers
#
# This Software is released under the MIT License:
# http://www.opensource.org/licenses/mit-license.html
# See license.txt for more details.
#
# $Id: html2safehtml.py 1072 2005-05-01 12:05:51Z ajung $

from HTMLParser import HTMLParser,HTMLParseError,piclose, charref, entityref
from string import lower,find

class HTML2SafeHTML(HTMLParser):
    
    can_close   = ['li','p','dd','dt','option']
    never_close = ['br','wbr','hr','input','isindex','base','meta','img']
    
    def __init__(self,valid_tags):
        HTMLParser.__init__(self)
        self.valid_tags = valid_tags
        self.result = ""
        self.openTags = []
        
    def end_tag(self,tag):
        self.result = f"{self.result}</{tag}>"
            
    def handle_data(self, data):
        if data:
            self.result = self.result + data

    def handle_charref(self, name):
        self.result = f"{self.result}&#{name};"
        
    from htmlentitydefs import entitydefs # our entity defs list to use
    
    def handle_entityref(self, name):
        # this quotes non-standard entities
        amp = '&' if self.entitydefs.has_key(name) else '&amp;'
        self.result = f"{self.result}{amp}{name};"

    def handle_starttag(self, tag, attrs):
        """ Delete all tags except for legal ones """

        if tag not in self.valid_tags:
            return
        self.result = f'{self.result}<{tag}'

        for k, v in attrs:
            if v is None:
                self.result += f' {k}'
            elif lower(k[:2]) != 'on' and lower(v[:10]) != 'javascript':
                self.result += ' %s="%s"' % (k, v)

        if tag not in self.never_close:
            self.openTags.append(tag)

        self.result = f'{self.result}>'
                
    def handle_endtag(self, tag):

        try:            

            while tag != self.openTags[-1] and self.openTags[-1] in self.can_close:
                self.openTags.pop()
            
            if tag==self.openTags[-1]:
                self.end_tag(self.openTags.pop())                
                
        except IndexError:
            pass

    def cleanup(self):
        """ Append missing closing tags """
        while self.openTags:
            tag = self.openTags.pop()
            if tag not in self.can_close:
                self.end_tag(tag)

    def parse_starttag(self,i):
        try:
            return HTMLParser.parse_starttag(self,i)
        except HTMLParseError:
            try:
                return piclose.search(self.rawdata,i).end()
            except AttributeError:
                return -1
        
    def parse_endtag(self,i):
        try:
            return HTMLParser.parse_endtag(self,i)
        except HTMLParseError:
            try:
                return piclose.search(self.rawdata,i).end()
            except:
                return -1

    def goahead(self,end):

        # fix incomplete entity and char refs        
        rawdata = self.rawdata

        i = 0
        n = len(rawdata)
        newdata=''

        while i < n:
            j = find(rawdata,'&',i)
            if j==-1:
                break
            newdata = newdata + rawdata[i:j]
            if charref.match(rawdata, j) or entityref.match(rawdata, j):
                newdata = f'{newdata}&'
            else:
                newdata = f'{newdata}&amp;'
            i = j+1

        self.rawdata = newdata + rawdata[i:]

        # do normal parsing
        try:
            return HTMLParser.goahead(self,end)
        except HTMLParseError:
            pass
        

