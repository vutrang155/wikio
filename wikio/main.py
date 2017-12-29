#!/usr/bin/env python
from wiki.Connection import connection
from wiki.wiki import Page
from wiki.wiki import Search
from wiki import  ErrorException
import sys
import wiki.meow


def run() :
    try :
        import argparse


        parser = argparse.ArgumentParser(prog='wikio', description='The program allows users to use Wikipedia through terminal screen using MediaWiki action API.\n'
                                                                  'The program is divided into two mode, find and get. In the get mode, the value in arguments'
                                                                  ' must\nbe passed by wiki\'s id, which is shown in find mode. Usage of the application can be indicated\n'
                                                                  'in the example below :\n\n'
                                                                  '   wikio -find David Bowie\n'
                                                                  '    Results for "David Bowie" :\n'
                                                                  '    1. David Bowie   [8786]...\n\n'
                                                                  '   wikio -get 8786\n'
                                                                  '    David Robert Jonnes (8 Janu...\n\n ',
                                                                  formatter_class=argparse.RawTextHelpFormatter)

        parser.add_argument('-find', help='find [name]', action='store_true')
        parser.add_argument('-get', help='get [id]', action='store_true')
        parser.add_argument('content', action='store', nargs='+', help='If the purpose is finding, the content will be a string. Otherwise it will be wiki\'s id which is found at -find')
        args = parser.parse_args()

        if (args.find and args.get) :

            print ('Two modes cannot be used in one time')

        elif args.find and args.get == False :

            s = ' '.join(args.content)
            print('Results for \"' + s + '\" : ')
            a = Search(s)
            print(a.toString())

        elif args.find == False and args.get :

            a = args.content[0]
            if wiki.meow.is_number(a) :
                pg = Page(int(a))
                if pg.nonValid :
                    raise ErrorException("Invalid id, Please try again with valid value")
                else :
                    print(pg.toString())
            else :
                raise ErrorException("Invalid value, The value must be a number")

    except ErrorException as e:
        import logging
        logger = logging.Logger('catch_all')
        logger.error('Error :  ' + str(e))

if __name__ == "__main__" :
    run()
