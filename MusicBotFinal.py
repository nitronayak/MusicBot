import vlc
import pafy
import urllib.request
import re
import youtube_dl
import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is the function called when the button is clicked
def btnClickFunction():
             getInputBoxValue()
             
# this is a function to get the user input from the text input box
def getInputBoxValue():
                rawsearch = SongName.get()
                search_keyword = rawsearch.replace(" ", "+")
                html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
                video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                url = ("https://www.youtube.com/watch?v=" + video_ids[0])
                video = pafy.new(url)
                best = video.getbest()
                playurl = best.url
                Instance = vlc.Instance()
                player = Instance.media_player_new()
                Media = Instance.media_new(playurl)
                Media.get_mrl()
                player.set_media(Media)
                player.play()
                

root = Tk()

# This is the section of code which creates the main window
root.geometry('1200x550')
root.configure(background='#ff3333')
root.title('MusicBot')

# This is the section of code which creates a listbox
listBoxOn=Listbox(root, bg='#F0F8FF', font=('arial', 12, 'normal'), width=0, height=0)
listBoxOn.insert('0', 'MusicBot by Nayak.')
listBoxOn.insert('1', 'Insert your video name into the text field below.')
listBoxOn.insert('2', 'While youtube tracks your usage and data, and sends them to advertisers, this player gets your videos anonymously.')
listBoxOn.insert('3', 'Note: VLC Player has to be installed')
listBoxOn.place(x=268, y=176)



# This is the section of code which creates a text input box
SongName=Entry(root)
SongName.place(x=32, y=498, height=30, width=1000)

# This is the section of code which creates a button
Button(root, text='Play Music', bg='#EEDFCC', font=('arial', 12, 'normal'), command=btnClickFunction).place(x= 1100, y=498)

root.mainloop()
