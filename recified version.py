__author__ = 'Administrator'
import urllib
import urllib2
import re

if __name__ == "__main__":

    url = 'http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1'
    page = urllib2.urlopen(url)
    html = page.read()
#title
    pattern = re.compile('<title>(.*?)</title>', re.S)
    title = re.search(pattern, html)
    print "title is: "+title.group(1).decode('utf-8')+'\n'

#stars
    pattern_guys = re.compile('<br><br>(.*?)<br>(.*?)<br>(.*?)<br>(.*?)<br>(.*?)<br>(.*?)</div><br>', re.S)
    guys = re.findall(pattern_guys, html)
    for guy in guys:
        print guy[0].decode('utf-8')

