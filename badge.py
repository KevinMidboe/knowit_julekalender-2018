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

def getPicture():
   with open("progress.svg", "rb") as imageFile:
      return imageFile.read()

def download_image(image_url):
   session = requests.Session()
   session.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"}

   r = session.get(image_url, stream=True, verify=False)
   with open('progress.svg', 'wb') as f:
      for chunk in r.iter_content(chunk_size=1024):
         f.write(chunk)

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

def uploadToDropbox(progress):
   dbx = dropbox.Dropbox(os.environ.get('DROPBOX_ACCESS_TOKEN'))

   response = dbx.files_upload(getPicture(), '/knowit/progress.svg', mode=WriteMode('overwrite', None))

def main():
   failures, total = get_xml_test_results()
   progress = "{0:.1f}".format((total-failures)/total * 100)
   color = getColor(progress)

   path = 'https://img.shields.io/badge/Progress-{}-{}.svg'.format(progress, color)
   download_image(path)

   print(progress)
   uploadToDropbox(progress)

if __name__ == '__main__':
   main()