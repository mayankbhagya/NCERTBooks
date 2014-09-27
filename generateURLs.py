import re

with open('source.js') as f:
    lines = f.readlines()

g_class=""
g_subject=""
g_book=""

for line in lines:
    line = line.strip()

    #subject line
    if ('==' in line):
        m = re.match('.*==([0-9]+).*=="([a-zA-Z ]+)".*', line)
        g = m.groups(0)
        g_class = g[0]
        g_subject = g[1]
    #line to be skipped
    elif 'document.test.tbook.options[0].text' in line:
        continue
    #name or url
    elif 'document.test.tbook.options' in line:
        #book name
        if '.text' in line:
            try:
                m = re.match('document.test.tbook.options\[[0-9]+\].text="([a-zA-Z \-()0-9\.&]+)".*', line)
                g = m.groups(0)
                g_book = g[0]
            except:
                pass
        #book url
        elif 'value' in line:
            try:
                m = re.match('document.test.tbook.options\[[0-9]+\].value="textbook.htm\?([a-z0-9]+)=0-([0-9]+)".*', line)
                g = m.groups(0)
                code = g[0]
                print g_class + '/' + g_subject + '/' + g_book + '|http://www.ncert.nic.in/ncerts/l/' + code + 'ps.pdf'
                for i in range(1, int(g[1])+1):
                    chapter = i
                    print g_class + '/' + g_subject + '/' + g_book + '|http://www.ncert.nic.in/ncerts/l/' + code + '%02d' % i + '.pdf'
            except:
                pass



'''
else if((document.test.tclass.value==12) && (document.test.tsubject.options[sind].text=="Sanskrit"))

    {

        document.test.tbook.options[0].text="..Select Book Title..";

        document.test.tbook.options[1].text="Bhaswati";

        document.test.tbook.options[1].value="textbook.htm?lhsk1=0-10"

            document.test.tbook.options[2].text="Shaswati";

        document.test.tbook.options[2].value="textbook.htm?lhsk2=0-12"

            document.test.tbook.options[3].text="";

        document.test.tbook.options[3].value=""

            

            }
'''
