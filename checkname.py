import re
import datetime

expression = '.*\W.*'
sp_expression = 'COM[0-9]|LPT[0-9]|CON|PRN|AUX|NUL|COM|LPT'

def fixname (_a):
    
    a = _a

    while(re.match(expression, a)):
        m = re.search('\W', a)
        a = a.replace(m.group(), '_')

    if(re.match(sp_expression, a)):
        a = 'N-hentai {0}'.format(datetime.datetime.now())

    return a