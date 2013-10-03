# -*- coding: utf-8 -*-  

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
import xml.dom.minidom
import re
import os.path

from BeautifulSoup import BeautifulSoup
import urllib
import urllib2
import random
import linecache

def read_word():
    count = len(open(os.path.dirname(__file__) + '\wordlist.txt','rU').readlines())
    hellonum=random.randrange(1,count, 1)
    return linecache.getline(os.path.dirname(__file__) + '\wordlist.txt',hellonum)



def is_hard_sentence(string, word):
    tmp = string.split(' ')
    fileHandle = open(os.path.dirname(__file__) + '\wordlist.txt','rU') 
    count = len(fileHandle.readlines())
    fileHandle.close()  
    for x in tmp:
        x = filter(str.isalpha, x).lower()
        for num in range(1,count):
            tmpword = linecache.getline(os.path.dirname(__file__) + '\wordlist.txt',num)
            tmpword = filter(str.isalpha, tmpword).lower()
            if cmp(x,tmpword) == 0 and cmp(x,word) == -1:
                print('yeeee!!!\n')
                fileHandle.close() 
                return 1

    fileHandle.close() 
    return 0




def request_word(request,word):
    url = "http://bnc.bl.uk/saraWeb.php?qy="+ word
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    soup = BeautifulSoup(res).find('div', id="solutions")
    sentences = []
    for x in soup.contents:
        if hasattr(x, 'contents'):
            if len(x.contents) >= 2:
                tmp = str(x.contents[1])
                tmp = tmp.split(' ')
                if len(tmp) > 15 and is_hard_sentence(str(x.contents[1]), word) == 0:
                    tmp2 = str(x.contents[1])
                    tmp2 = tmp2.replace(str(word),'_____')
                    sentences.append(tmp2)
                if len(sentences) >= 3:
                    break

    t = get_template('WordTmpl.py')
    word = read_word();
    html = t.render(Context({'stces': '', 'main': sentences, 'newword': word}))
    return HttpResponse(html)