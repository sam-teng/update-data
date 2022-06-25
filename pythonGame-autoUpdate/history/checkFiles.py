import os
import time
import wget,sys
import urllib #urllib2.urlopen 

import requests

fn = None
data = ""

# ------
import zipfile #zipfile.ZipFile
if fn == None:
  if len(list(data)) == 0:
    yt_urls = input("enter your file's full url")
  else:
    yt_urls = data
  yt_urls = yt_urls.split(",")
  i = 0
  yt_title = []
  print("wget is on path %s" % (wget.__file__))
  for yt_url in yt_urls:
    if yt_url == "":
      yt_url = "https://ppt.cc/f3WMBx"
    try:
      url = yt_url
      r = requests.get(url, auth=('user', 'pass'))#https://api.github.com
      print(r.status_code)
      print(r.headers['content-type'])
      req = urllib2.Request(url)
      downloadurl = urllib2.urlopen(req)
      zipcontent = downloadurl.read()
      with open("%d."+input("請輸入副檔名")%(i), 'wb') as f:
          f.write(zipcontent)
      #w = wget.download(url,out="\\"+i+".rar")
      """
      yt = YouTube(yt_url)#YouTube('https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ')
      print('strart downloads: ',yt.title)
      path = ""#yt.title
      #yt_title = yt_title.join(yt.title)
      yt_title.append(yt.title)
      """
      """
      if not os.path.exists(path):
        os.makedirs(path)
      """
      #print(type(yt))
      """
      yt.streams.filter(subtype='mp4').first().download(path)#
      print('finish',yt.title,'downloads!')
      """
    except:
      print("can't from" + yt_url + "\t download file")
      #yt_title.remove(yt.title)
    finally:
      i = i + 1
      time.sleep(3)
else:
  pass