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


#Current tags
#fanbox id:noritamagomyon
#fanbox post id:2973393_【r-18】チラ見せして誘惑してくる幽々子様
#fanbox post id:1604673
#fanbox user number:2468289

#Sample json file:
##"category": "fanbox",
##    "commentCount": 2,
##    "coverImageUrl": "https://pixiv.pximg.net/c/1200x630_90_a2_g5/fanbox/public/images/post/441198/cover/P0DRcCMB9mkCVK54vEZ1j1Rz.jpeg",
##    "creatorId": "ranthath",
##    "date": "2019-06-25 18:08:40",
##    "excerpt": "えっちなフランちゃんです",
##    "extension": "jpg",
##    "feeRequired": 0,
##    "fileUrl": "https://pixiv.pximg.net/c/1200x630_90_a2_g5/fanbox/public/images/post/441198/cover/P0DRcCMB9mkCVK54vEZ1j1Rz.jpeg",
##    "filename": "P0DRcCMB9mkCVK54vEZ1j1Rz",
##    "hasAdultContent": true,
##    "id": "441198",
##    "isCoverImage": true,
##    "isLiked": false,
##    "isRestricted": false,
##    "likeCount": 84,
##    "num": 0,
##    "publishedDatetime": "2019-06-26T03:08:40+09:00",
##    "restrictedFor": null,
##    "subcategory": "creator",
##    "tags": [],
##    "text": "えっちなフランちゃんです",
##    "title": "ふらんたそ～",
##    "type": "image",
##    "updatedDatetime": "2019-06-26T03:16:34+09:00",
##    "user": {
##        "iconUrl": "https://pixiv.pximg.net/c/160x160_90_a2_g5/fanbox/public/images/user/536764/icon/FazLeiRl1HU0rMJ5VK27RMKs.jpeg",
##        "name": "みよ",
##        "userId": "536764"

##Another sample:
##{
##    "articleBody": {
##        "blocks": [
##            {
##                "text": "",
##                "type": "p"
##            },
##            {
##                "imageId": "rreliAExQfMGl8OS7CEZ9BO6",
##                "type": "image"
##            },
##            {
##                "text": "",
##                "type": "p"
##            },
##            {
##                "imageId": "JaK9JPMHDcDniCQUd1v4dRK8",
##                "type": "image"
##            },
##            {
##                "text": "",
##                "type": "p"
##            },
##            {
##                "imageId": "6iufcsdeXYp5uAmGMypkmklW",
##                "type": "image"
##            },
##            {
##                "text": "",
##                "type": "p"
##            },
##            {
##                "imageId": "tKU7IxEcG9f6bz1EevXZXttI",
##                "type": "image"
##            },
##            {
##                "text": "",
##                "type": "p"
##            },
##            {
##                "imageId": "9Rg6PUcQ3RLEN5UwQloBISPt",
##                "type": "image"
##            },
##            {
##                "text": "",
##                "type": "p"
##            },
##            {
##                "imageId": "7XEHDKSVEOjfUaOd0PfqDTII",
##                "type": "image"
##            },
##            {
##                "text": "",
##                "type": "p"
##            },
##            {
##                "text": "セリフなしVer.",
##                "type": "p"
##            },
##            {
##                "imageId": "rnPlBhxnw6tKi4jWUOvDkS9a",
##                "type": "image"
##            },
##            {
##                "text": "",
##                "type": "p"
##            },
##            {
##                "imageId": "nHxYAYNbqRPPYv5UtYxBUjKS",
##                "type": "image"
##            },
##            {
##                "text": "",
##                "type": "p"
##            },
##            {
##                "imageId": "dg5gJOJge1KeP4ni2S1kQFqr",
##                "type": "image"
##            },
##            {
##                "text": "",
##                "type": "p"
##            },
##            {
##                "imageId": "PBOhQpmtZaIsSAWDjUhZZtYn",
##                "type": "image"
##            },
##            {
##                "text": "",
##                "type": "p"
##            },
##            {
##                "imageId": "Gr1H1DwP3RD10sxlWmPNl6zS",
##                "type": "image"
##            },
##            {
##                "text": "",
##                "type": "p"
##            },
##            {
##                "imageId": "rPhiyCl7SgO7MiOy2TJ7lQl1",
##                "type": "image"
##            },
##            {
##                "text": "",
##                "type": "p"
##            },
##            {
##                "text": "",
##                "type": "p"
##            },
##            {
##                "text": "今回もご覧くださり誠にありがとうございます！",
##                "type": "p"
##            },
##            {
##                "text": "本当に励みになっております…！",
##                "type": "p"
##            },
##            {
##                "text": "",
##                "type": "p"
##            },
##            {
##                "text": "今回は体格差のある2人の百合が描きたかった話です…",
##                "type": "p"
##            },
##            {
##                "text": "正反対な2人の関係性って尊いですよね…(*´-`)",
##                "type": "p"
##            }
##        ],
##        "embedMap": {},
##        "fileMap": {},
##        "imageMap": {
##            "6iufcsdeXYp5uAmGMypkmklW": {
##                "extension": "jpeg",
##                "height": 2150,
##                "id": "6iufcsdeXYp5uAmGMypkmklW",
##                "originalUrl": "https://downloads.fanbox.cc/images/post/3029955/6iufcsdeXYp5uAmGMypkmklW.jpeg",
##                "thumbnailUrl": "https://downloads.fanbox.cc/images/post/3029955/w/1200/6iufcsdeXYp5uAmGMypkmklW.jpeg",
##                "width": 1518
##            },
##            "7XEHDKSVEOjfUaOd0PfqDTII": {
##                "extension": "jpeg",
##                "height": 2150,
##                "id": "7XEHDKSVEOjfUaOd0PfqDTII",
##                "originalUrl": "https://downloads.fanbox.cc/images/post/3029955/7XEHDKSVEOjfUaOd0PfqDTII.jpeg",
##                "thumbnailUrl": "https://downloads.fanbox.cc/images/post/3029955/w/1200/7XEHDKSVEOjfUaOd0PfqDTII.jpeg",
##                "width": 1518
##            },
##            "9Rg6PUcQ3RLEN5UwQloBISPt": {
##                "extension": "jpeg",
##                "height": 2150,
##                "id": "9Rg6PUcQ3RLEN5UwQloBISPt",
##                "originalUrl": "https://downloads.fanbox.cc/images/post/3029955/9Rg6PUcQ3RLEN5UwQloBISPt.jpeg",
##                "thumbnailUrl": "https://downloads.fanbox.cc/images/post/3029955/w/1200/9Rg6PUcQ3RLEN5UwQloBISPt.jpeg",
##                "width": 1518
##            },
##            "Gr1H1DwP3RD10sxlWmPNl6zS": {
##                "extension": "jpeg",
##                "height": 2150,
##                "id": "Gr1H1DwP3RD10sxlWmPNl6zS",
##                "originalUrl": "https://downloads.fanbox.cc/images/post/3029955/Gr1H1DwP3RD10sxlWmPNl6zS.jpeg",
##                "thumbnailUrl": "https://downloads.fanbox.cc/images/post/3029955/w/1200/Gr1H1DwP3RD10sxlWmPNl6zS.jpeg",
##                "width": 1518
##            },
##            "JaK9JPMHDcDniCQUd1v4dRK8": {
##                "extension": "jpeg",
##                "height": 2150,
##                "id": "JaK9JPMHDcDniCQUd1v4dRK8",
##                "originalUrl": "https://downloads.fanbox.cc/images/post/3029955/JaK9JPMHDcDniCQUd1v4dRK8.jpeg",
##                "thumbnailUrl": "https://downloads.fanbox.cc/images/post/3029955/w/1200/JaK9JPMHDcDniCQUd1v4dRK8.jpeg",
##                "width": 1518
##            },
##            "PBOhQpmtZaIsSAWDjUhZZtYn": {
##                "extension": "jpeg",
##                "height": 2150,
##                "id": "PBOhQpmtZaIsSAWDjUhZZtYn",
##                "originalUrl": "https://downloads.fanbox.cc/images/post/3029955/PBOhQpmtZaIsSAWDjUhZZtYn.jpeg",
##                "thumbnailUrl": "https://downloads.fanbox.cc/images/post/3029955/w/1200/PBOhQpmtZaIsSAWDjUhZZtYn.jpeg",
##                "width": 1518
##            },
##            "dg5gJOJge1KeP4ni2S1kQFqr": {
##                "extension": "jpeg",
##                "height": 2150,
##                "id": "dg5gJOJge1KeP4ni2S1kQFqr",
##                "originalUrl": "https://downloads.fanbox.cc/images/post/3029955/dg5gJOJge1KeP4ni2S1kQFqr.jpeg",
##                "thumbnailUrl": "https://downloads.fanbox.cc/images/post/3029955/w/1200/dg5gJOJge1KeP4ni2S1kQFqr.jpeg",
##                "width": 1518
##            },
##            "nHxYAYNbqRPPYv5UtYxBUjKS": {
##                "extension": "jpeg",
##                "height": 2150,
##                "id": "nHxYAYNbqRPPYv5UtYxBUjKS",
##                "originalUrl": "https://downloads.fanbox.cc/images/post/3029955/nHxYAYNbqRPPYv5UtYxBUjKS.jpeg",
##                "thumbnailUrl": "https://downloads.fanbox.cc/images/post/3029955/w/1200/nHxYAYNbqRPPYv5UtYxBUjKS.jpeg",
##                "width": 1518
##            },
##            "rPhiyCl7SgO7MiOy2TJ7lQl1": {
##                "extension": "jpeg",
##                "height": 2150,
##                "id": "rPhiyCl7SgO7MiOy2TJ7lQl1",
##                "originalUrl": "https://downloads.fanbox.cc/images/post/3029955/rPhiyCl7SgO7MiOy2TJ7lQl1.jpeg",
##                "thumbnailUrl": "https://downloads.fanbox.cc/images/post/3029955/w/1200/rPhiyCl7SgO7MiOy2TJ7lQl1.jpeg",
##                "width": 1518
##            },
##            "rnPlBhxnw6tKi4jWUOvDkS9a": {
##                "extension": "jpeg",
##                "height": 2150,
##                "id": "rnPlBhxnw6tKi4jWUOvDkS9a",
##                "originalUrl": "https://downloads.fanbox.cc/images/post/3029955/rnPlBhxnw6tKi4jWUOvDkS9a.jpeg",
##                "thumbnailUrl": "https://downloads.fanbox.cc/images/post/3029955/w/1200/rnPlBhxnw6tKi4jWUOvDkS9a.jpeg",
##                "width": 1518
##            },
##            "rreliAExQfMGl8OS7CEZ9BO6": {
##                "extension": "jpeg",
##                "height": 2150,
##                "id": "rreliAExQfMGl8OS7CEZ9BO6",
##                "originalUrl": "https://downloads.fanbox.cc/images/post/3029955/rreliAExQfMGl8OS7CEZ9BO6.jpeg",
##                "thumbnailUrl": "https://downloads.fanbox.cc/images/post/3029955/w/1200/rreliAExQfMGl8OS7CEZ9BO6.jpeg",
##                "width": 1518
##            },
##            "tKU7IxEcG9f6bz1EevXZXttI": {
##                "extension": "jpeg",
##                "height": 2150,
##                "id": "tKU7IxEcG9f6bz1EevXZXttI",
##                "originalUrl": "https://downloads.fanbox.cc/images/post/3029955/tKU7IxEcG9f6bz1EevXZXttI.jpeg",
##                "thumbnailUrl": "https://downloads.fanbox.cc/images/post/3029955/w/1200/tKU7IxEcG9f6bz1EevXZXttI.jpeg",
##                "width": 1518
##            }
##        },
##        "urlEmbedMap": {}
##    },
##    "category": "fanbox",
##    "commentCount": 17,
##    "coverImageUrl": "https://pixiv.pximg.net/c/1200x630_90_a2_g5/fanbox/public/images/post/3029955/cover/zXL1XfEoQmhKXoDmjoi34vMU.jpeg",
##    "creatorId": "yuruyunaznk",
##    "date": "2021-11-21 11:00:10",
##    "excerpt": "セリフなしVer.\n今回もご覧くださり誠にありがとうございます！\n本当に励みになっております…！\n今回は体格差のある2人の百合が描きたかった話です…\n正反対な2人の関係性って尊いですよね…(*´-`)",
##    "extension": "jpg",
##    "feeRequired": 200,
##    "fileId": "9Rg6PUcQ3RLEN5UwQloBISPt",
##    "fileUrl": "https://downloads.fanbox.cc/images/post/3029955/9Rg6PUcQ3RLEN5UwQloBISPt.jpeg",
##    "filename": "9Rg6PUcQ3RLEN5UwQloBISPt",
##    "hasAdultContent": true,
##    "height": 2150,
##    "id": "3029955",
##    "isCoverImage": false,
##    "isLiked": false,
##    "isRestricted": false,
##    "likeCount": 86,
##    "num": 3,
##    "publishedDatetime": "2021-11-21T20:00:10+09:00",
##    "restrictedFor": null,
##    "subcategory": "creator",
##    "tags": [
##        "FANBOX限定漫画"
##    ],
##    "text": null,
##    "title": "メイドさんに興味津々なお嬢様(R18) ",
##    "type": "article",
##    "updatedDatetime": "2021-11-21T20:00:10+09:00",
##    "user": {
##        "iconUrl": "https://pixiv.pximg.net/c/160x160_90_a2_g5/fanbox/public/images/user/14188490/icon/z0K2mVpba3LLlNdGMui8hMTz.jpeg",
##        "name": "ざんか",
##        "userId": "14188490"
##    },
##    "width": 1518
##}

##logging.debug("File: {}\nType: {}".format(infile, type(fbx['user'])))

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


