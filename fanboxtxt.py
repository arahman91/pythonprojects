import sys
import json
import os
import logging

logging.basicConfig(level=logging.DEBUG)

infile = str(sys.argv[1]) + '.json'
tagfile = str(sys.argv[1]) + '.txt'
htmlfile = str(sys.argv[1]) + '.html'

#logging.debug("Tagfile: {}".format(tagfile))

with open(infile, encoding='utf-8') as fanbox:
    fbx = json.load(fanbox)

tags = "fanbox user number:" + str(fbx['user']['userId']) + "\nfanbox post id:" + str(fbx['id'])
tags = tags + "\nfanbox id:" + fbx['creatorId'] + "\nfanbox file name:" + fbx['filename']
tags = tags + "\ntitle:" +  fbx['title'] + "\nnum:" +  str(fbx['num'] ) + "\npage:" +  str(fbx['num'] )
if fbx['tags']:
    for i in fbx['tags']:
        tags = tags + "\n" + i

if not os.path.isfile(tagfile):
    with open(tagfile, 'w', encoding='utf-8') as e:
        e.write(tags)
    logging.debug("File written: {}".format(tagfile))
else:
    logging.debug("File exists: {}".format(tagfile))

htmlimage =  os.path.basename(str(sys.argv[1]))

htmlstyle= "* {\n" +\
           "margin: 0;\n"+\
           "padding: 0;\n"+\
           "}\n" +\
           ".imgbox {\n"+\
           "display: grid;\n"+\
           "height: 100%;\n"+\
           "}\n"+\
           ".center-fit {\n"+\
           "max-width: 100%;\n"+\
           "max-height: 100vh;\n"+\
           "margin: auto;\n"+\
           "}\n" +\
           ".textpart {\n" +\
           "text-align: center;\n"+\
           "font-size: x-large;\n"+\
           "font-family: Arial, Helvetica, sans-serif;\n"+\
           "}\n"

if fbx['title']:
    title = fbx['title']
else:
    title = ""

if fbx['excerpt']:
    content = fbx['excerpt'].replace("\n", "<br>")
else:
    content = ""

titleurl = "https://www.pixiv.net/fanbox/creator/"+ str(fbx['user']['userId']) + "/post/" + str(fbx['id'])

html = ("<!DOCTYPE html>\n"+\
        "<html>\n"+\
        "<head>\n"+\
        "<meta charset=\"UTF-8\">\n"+\
        "<style>\n"+\
        htmlstyle + "\n"+\
        "</style>\n"\
        "<title>" + title + \
        "\n</title>\n"+\
        "</head>\n"+\
        "<body>\n"+\
        "<div class=\"textpart\">\n" +\
        "<h1><a href=\""+ titleurl + "\">" + title + "</a></h1><br>\n"+\
        "</div>\n" +\
        "<p>\n" +\
        "<div class=\"imgbox\">\n" +\
        "<img class=\"center-fit\" src=\"" + htmlimage + "\" alt=" + htmlimage + "\">\n" +\
        "</div>\n" +\
        "</p><br>\n" + \
        "<div class=\"textpart\">\n" +\
        "<p>" + content +"</p>\n"+\
        "</div>\n" +\
        "</body>\n"+\
        "</html>\n").replace("class=\\","class=")

if not os.path.isfile(htmlfile):
    with open(htmlfile, 'w', encoding='utf-8') as h:
        h.write(html)
    logging.debug("File written: {}".format(htmlfile))
else:
    logging.debug("File exists: {}".format(htmlfile))


