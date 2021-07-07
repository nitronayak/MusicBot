import vlc
import pafy
import urllib.request
import re
import youtube_dl

print ("Welcome to MusicBot: Developed by Nayak.")
print ("Do you want instructions and requirements? (y/n) ")
userchoice= input()
if userchoice == "y":
    print ("Enter the song name in the field given below. Make sure that you have VLC media player installed. Using this media player will help in protecting your viewing history and preferences from Youtube. Completely secure and incognito.")
elif userchoice == "n":
    print("Welcome back to MusicBot!")
else:
    print ("Option invalid. Continuing without instructions.")    

    
rawsearch = input ("Input the song you want to play from Youtube: ")
search_keyword = rawsearch.replace(" ", "+")
print("Searching for most relavant video...")
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
url = ("https://www.youtube.com/watch?v=" + video_ids[0])

video = pafy.new(url)
best = video.getbest()
playurl = best.url
print ("Success finding Track!")
Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()



