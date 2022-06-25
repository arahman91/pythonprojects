import sys
import json
import os
import logging

infile = str(sys.argv[1]) + '.json'
outfile = str(sys.argv[1]) + '.txt'
outhtml = str(sys.argv[1]) + ".html"

logging.basicConfig(level=logging.DEBUG)

with open(infile, encoding='utf-8') as kemono:
    kn = json.load(kemono)

taglist = "discord post id:" + str(kn['id']) + "\ndiscord user id:" + str(kn['author']['id']) + \
          "\ndiscord user name:" + kn['author']['username'] + \
          "\npost number:" + str(kn['num']) 

with open(outfile, 'w', encoding='utf-8') as f:
    f.write(taglist)
logging.debug("File written: {}".format(outfile))

htmlimage = str(sys.argv[1])

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

htmlfile = "<!DOCTYPE html>\n" +\
           "<html>\n" +\
           "<head>\n" +\
           "<meta charset=\"UTF-8\">\n" +\
           "<style>\n"+\
           htmlstyle + "\n"+\
           "</style>\n"\
           "</head>\n" +\
           "<body><p>\n" +\
           "<div class=\"imgbox\">\n" +\
           "<img class=\"center-fit\" src=\"" + htmlimage + "\" alt=" + htmlimage + "\">\n" +\
           "</div>\n" +\
           "</p><br>\n" + \
           "<div class=\"textpart\">\n" +\
           "<p>\n" + \
           str(kn['content']).replace("\n", "<br>")  + "\n" +\
           "</p>\n"+\
           "</div>\n" +\
           "</body>\n"+\
           "</html>"

with open(outhtml, 'w', encoding='utf-8') as h:
    h.write(htmlfile)
logging.debug("File written: {}".format(outhtml))
