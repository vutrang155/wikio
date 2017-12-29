###############################- Initialisation -#####################################
import json
import codecs
import sys


from Connection import connection
from meow import *
from ErrorException import *
from colors import bcolors

#Problems about Unicode
try:
    # python 3
    sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
except:
    # python 2
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)


####################################################################################



class Page :

    def __init__(self, pageId) :

        self.connect = connection.getInstance()
        self.pageId = pageId
        self.getter = self.connect.get("getbyId", self.pageId)
        self.nonValid = False

        try :
            self.getter["query"]["pages"][str(self.pageId)]["extract"]
        except Exception :
            self.nonValid = True


    #Return Content
    def content(self) :

        if self.nonValid != True :
            return self.getter["query"]["pages"][str(self.pageId)]["extract"]
        else :
            return -1


    #Return title
    def title(self) :

        if self.nonValid != True :
            return self.getter["query"]["pages"][str(self.pageId)]["title"]
        else :
            return -1


    def toString(self) :

        ret = '\n ' + bcolors.GREEN + str(self.title()) + bcolors.ENDC + '    [' + bcolors.YELLOW + str(self.pageId) + bcolors.ENDC + ']\n\n' + reindent(str(self.content()), 4)
        return ret




class Search :

    def __init__(self, stri) :

        self.list_pages = list()
        self.list_pagess = list()
        self.connect = connection.getInstance()
        self.str = stri

        getter = self.connect.get("search", self.str )
        self.length = len(getter["query"]["search"])

        for i in range(0, self.length) :
            self.list_pages.append( Page( getter["query"]["search"][i]["pageid"] ) )
            self.list_pagess.append(getter["query"]["search"][i])


    def getTitle(self, ids) :

        if ids < 0 or ids >= self.length :
            raise ErrorException('id must be higher than 0 and lower than'+str(self.length))
        elif self.length == 0 :
            raise ErrorException('There\'s no result')
        else:
            return self.list_pages[ids]["title"]


    def getContent(self, ids) :

        if ids < 0 or ids >= self.length :
            raise ErrorException('id must be higher than 0 and lower than'+str(self.length))
        elif self.length == 0 :
            raise ErrorException('There\'s no result')
        else:
            return self.list_pagess[ids]["snippet"]


    def toString(self) :

        ret = ''
        for i in range(0, self.length) :
            ret += str(i+1) + '. ' + bcolors.GREEN + str(self.list_pages[i].title()) + bcolors.ENDC +  '   [' + bcolors.YELLOW + str(self.list_pages[i].pageId) + bcolors.ENDC +']\n'+ reindent(remove_tags(self.getContent(i)),4) + '\n\n'

        return ret
