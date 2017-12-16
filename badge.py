#!/usr/bin/env python3.6
import os, dropbox, requests
import xml.etree.ElementTree as ET
from dropbox.files import WriteMode

from colour import Color

def get_xml_test_results():
   tree = ET.parse('result.xml')
   root = tree.getroot()
   failures = int(root.attrib['failures'])
   total = int(root.attrib['tests'])
   return [failures, total]

def buildURL(subject, value, color):
   return 'https://img.shields.io/badge/{}-{}-{}.svg'.format(subject, value, color)

def getPicture(path):
   with open(path, "rb") as imageFile:
      return imageFile.read()

def downloadImage(image_url):
   session = requests.Session()
   session.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"}
   localFilename = image_url.split('/')[-1].split("?")[0].split('-')[0].lower() + '.svg'
   print(localFilename)
   exit(0)

   r = session.get(image_url, stream=True, verify=False)
   with open(localFilename, 'wb') as f:
      for chunk in r.iter_content(chunk_size=1024):
         f.write(chunk)

   return localFilename

def getColor(value):
   start = Color('red')
   end = Color('yellowgreen')
   colors = list(start.range_to(Color(end), 10))
   hexList = []
   for color in colors:
      if not str(color)[:1] is '#':
         hexList.append(color.hex[1:])
      else:
         hexList.append(str(color)[1:])

      if (len(hexList[-1]) <= 4):
         hexList[-1] = hexList[-1] + '000'
   
   return hexList[int(float(value)/10)]

def uploadToDropbox(path):
   dbx = dropbox.Dropbox(os.environ.get('DROPBOX_ACCESS_TOKEN'))
   response = dbx.files_upload(getPicture(path), '/knowit/' + path, mode=WriteMode('overwrite', None))

def main():
   failures, total = get_xml_test_results()
   progress = "{0:.1f}".format((total-failures)/total * 100)
   completed = str(total-failures) + '_of_' + str(total)
   color = getColor(progress)

   image1 = downloadImage(buildURL('Progress', progress + '%25', color))
   image2 = downloadImage(buildURL('Completed', completed, color))

   uploadToDropbox(image1)
   uploadToDropbox(image2)

if __name__ == '__main__':
   main()