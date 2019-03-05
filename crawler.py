from urllib import request
import requests
import re
from bs4 import BeautifulSoup
from pprint import pprint
import urllib,time
 
def get_content(url):
        headers = {
                'Host': 'music.163.com',
                'Referer': 'https://music.163.com/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
        }
        r = requests.session()
        r = BeautifulSoup(r.get(url, headers=headers).content, "html.parser")
        return r
 
def save(r):
        music_dict = {}
        result = r.find('ul', {'class': 'f-hide'}).find_all('a')
        #print(result)
        for music in result:
                music_dict[music['href'].strip("/song?id=")] = music.text
        #for k, v in src_dict.items():
            #print(k, v)
        return music_dict
 
def download_song(song_id,music_dict):
    try:
        song_url = 'http://music.163.com/song/media/outer/url?id=%s.mp3'%song_id  #该链接为浏览器在网页版缓存歌曲的下载链接
            #song_content=get_content(song_url)
            #print(song_content)
            #urllib.request.urlretrieve(song_url, r'C:\Users\Administrator\Desktop\%s.mp3'%music_dict[song_id])  # 下载文件
            #request.urlretrieve(song_url, r'C:\Users\Administrator\Desktop\%S.mp3'%music_dict[song_id])
        urllib.request.urlretrieve(song_url,'D:\\test\\%s.mp3'%music_dict[song_id])
        time.sleep(0.9)
        print("下载完成!")
    except KeyError:
        print("请确认歌曲id是否正确或者歌曲是否收费。")
 
def write(music_dict):
    fp = open('music1.txt', 'a')
    for k, v in music_dict.items():
        fp.write(music_dict[k] + "\r\n" + "id:" + k + "\r\n")
    fp.close()
 
if __name__ == '__main__':
        url = 'https://music.163.com/playlist?id=2252736518'
        r=get_content(url)
        music_dict=save(r)
        pprint(music_dict)
        #print(musiclist[5]+"\r\n"+musiclist[6])
        write(music_dict)
        print("---------------------")
        while 1:
            song_id = input("(输入0退出)请输入想下载的歌曲id:")
            if song_id=='0':
                print("欢迎使用")
                break
            print("正在搜索歌曲信息并下载.")
        #musiclist=",".join(musiclist)
            download_song(song_id,music_dict)
 
 
 
 
 
 
 
 
 
