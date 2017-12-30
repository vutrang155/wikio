import re
import string

def remove_tags(text):

  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', text)
  return cleantext

def is_number(s):

    try:
        int(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
        return False


def reindent(s, numSpaces):

    s = s.split('\n')
    try :
        s = [(numSpaces * ' ') + str.lstrip(line) for line in s]
    except (TypeError) :
        s = [(numSpaces * ' ') + unicode.lstrip(line) for line in s]
    s = '\n'.join(s)
    return s
