import os
import time
import wget,sys
import urllib #urllib2.urlopen 

import requests

fn = None
data = """
        https://github.com/sam-teng/update-data/blob/main/pythonGame-autoUpdate/game_socket-client_2P-GUIv2.py,
        https://github.com/sam-teng/update-data/blob/main/pythonGame-autoUpdate/game_socket-server_2P-GUIv2.py,
        https://github.com/sam-teng/update-data/blob/main/pythonGame-autoUpdate/view.py
       """

# ------
import zipfile #zipfile.ZipFile
if fn == None:
  if len(list(data)) == 0:
    yt_urls = input("enter your file's full url")
  else:
    yt_urls = data
  yt_urls = yt_urls.split(",")
  i = 0
  yt_title = []
  print("wget is on path %s" % (wget.__file__))
  for yt_url in yt_urls:
    if yt_url == "":
      yt_url = "https://drive.google.com/file/d/1SXwx5E9fO_RuEaGMhaykhKBI3MPDXg-h/view?usp=sharing"
    try:
      url = yt_url
      r = requests.get(url)#, auth=('sam-teng', 'teng1067'))#https://api.github.com
      print(r.status_code)
      print(r.headers['content-type'])

      
      print(i)
      urllib.request.urlretrieve(url, "%d.py"%(i))
      #req = urllib.request(url)
      
      #downloadurl = urllib.urlopen(req)
      
      #zipcontent = downloadurl.read()
      #with open("%d."%(i), 'wb') as f:
          #f.write(zipcontent)
      
      #w = wget.download(url,out=""+i+".py")
      
      """
      yt = YouTube(yt_url)#YouTube('https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ')
      print('strart downloads: ',yt.title)
      path = ""#yt.title
      #yt_title = yt_title.join(yt.title)
      yt_title.append(yt.title)
      """
      """
      if not os.path.exists(path):
        os.makedirs(path)
      """
      #print(type(yt))
      """
      yt.streams.filter(subtype='mp4').first().download(path)#
      print('finish',yt.title,'downloads!')
      """
    except:
      print("can't from" + yt_url + "\t download file")
      #yt_title.remove(yt.title)
    finally:
      i = i + 1
      time.sleep(3)
else:
  pass
