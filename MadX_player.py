from cProfile import label
from distutils.command.config import config
from email.mime import image
from math import fabs
from re import T
from tkinter import ttk
import pygame
from pygame import mixer
from tkinter import *
import os
import time
from mutagen.mp3 import MP3
from tkinter import filedialog
from PIL import Image, ImageTk

#Current time duration function
def song_duration():
    current_time =mixer.music.get_pos() / 1000

    #Song duration to time
    converte_song_time = time.strftime('%H:%M:%S', time.gmtime(current_time))

#get currently playing song
    current_song = playlist.curselection()
    song = playlist.get(current_song)

    song= f'C:/Users/Mr.MadX/Desktop/Madx/{song}.mp3'

    song_mutg = MP3(song)
    #making song length gloable
    global song_length
    song_length = song_mutg.info.length
    converte_song_length = time.strftime('%H:%M:%S', time.gmtime(song_length))

    song_full_time.config(text= converte_song_length)

    song_timer.config(text=converte_song_time)
    
    #song slider staring velue as song current time
    songslider.config(value=int(current_time))
    
    #song timer refresh after 1 second
    song_timer.after(1000, song_duration)

# Add manny songs to the playlist
def add_song():
    song = filedialog.askopenfilenames(initialdir=r'C:\Users\Mr.MadX\Desktop\Madx', title="ChooseA Song", filetypes=(("mp3 file","*mp3"), ))
#Creating for loop to add multiple songs in one time
    for song in song:
        song = song.replace("C:/Users/Mr.MadX/Desktop/Madx/", "")
        song = song.replace(".mp3","")
#Insert songs in playlist
        playlist.insert(END, song)

#Play function

def playsong():
    song = playlist.get(ACTIVE)
    song = f'C:/Users/Mr.MadX/Desktop/Madx/{song}.mp3'
   
    mixer.music.load(song)
    mixer.music.play(loops=0)
    #auto higlight the first song in playlist
    playlist.selection_set(ACTIVE)
    
    #Calling the song deruation when we click play
    song_duration()

    #Creating new var for song position and length of the song
    slider_position = int(song_length)
    songslider.config(to=slider_position, value=0)

#Creating gloabal pause variable
global paused
paused = False

#Pause/ Unpause function in one button

def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        mixer.music.unpause()
        paused = False
    else:
        mixer.music.pause()
        paused = True

#Volume control function

def vol(x):
    mixer.music.set_volume(volslider.get())


#Song forword function
def forword():
    #To get the the velue of current selected song 
    next_song = playlist.curselection()
    #adding 1 to current song to get next song
    next_song = next_song[0]+1
    song = playlist.get(next_song)
    song = f'C:/Users/Mr.MadX/Desktop/Madx/{song}.mp3'
   
    mixer.music.load(song)
    mixer.music.play()
    
    #Clearing the current selection onn playlist
    playlist.selection_clear(0, END)
    playlist.activate(next_song)
    #re selecting the next song
    playlist.selection_set(next_song)

#Song Backward function
def Backward():
    #To get the the velue of current selected song
    previous_song = playlist.curselection()

    #subtracting 1 in current song to get previous song
    previous_song = previous_song[0]-1
    song = playlist.get(previous_song)
    song = f'C:/Users/Mr.MadX/Desktop/Madx/{song}.mp3'
   
    mixer.music.load(song)
    mixer.music.play()
    
    #Clearing the current selection onn playlist
    playlist.selection_clear(0, END)
    playlist.activate(previous_song)
    #re selecting the next songong)
    playlist.selection_set(previous_song)

#Delete one song function
def delete_song():
    #deleting the selected song
    playlist.delete(ANCHOR)
    #stop the song
    mixer.music.stop()

#Delete all songs from playlist
def delete_songs():
    #Deleting all songs present in the playlist
    playlist.delete(0, END)
    #stop the song
    mixer.music.stop()


#Song slider function
def song_slider(x):
    #get the active song in from playlist
    song = playlist.get(ACTIVE)
    song = f'C:/Users/Mr.MadX/Desktop/Madx/{song}.mp3'

    #loding it on slider
    mixer.music.load(song)
    mixer.music.play(loops=0, start=int(songslider.get()))

#Root frame
root = Tk()
#title of appliction
root.title("MadX Player")
#App layout is not resizeable
root.resizable(False,False)
#App layout
root.geometry('400x690')
#icon of our app
icon = PhotoImage(file=r"C:\Users\Mr.MadX\KL\MadX_Player\Icon_and_img\madx_logo.png")
root.iconphoto(True,icon)

#Background image in a canvas
bg = ImageTk.PhotoImage(file=r"C:\Users\Mr.MadX\KL\MadX_Player\Icon_and_img\kl.jpg")
new_cnv = Canvas(root, width=400, height=690)
new_cnv.pack(fill="both", expand=False)

#Set image in canvas
new_cnv.create_image(0,0,image= bg, anchor="nw")

#top image on canvas background
top = ImageTk.PhotoImage(file=r"C:\Users\Mr.MadX\KL\MadX_Player\Icon_and_img\hgmadx.png")
new_cnv.create_image(200,150,image= top, anchor="center")

#Playlist box layout and design
playlist = Listbox(root,selectmode=SINGLE,bg= "black",fg="blue", font=('Comic Sans MS',12))
playlist.place(x=20,y=290,relheight=0.3,relwidth=0.9)

#Volume outline frame
volframewin = new_cnv.create_text(352,550, anchor="nw", text="VOL",fill= "orange")

#Initializing the mixer module
mixer.init()

#Define Button Icon
#-------------------------------------------
#Play button
p1 = ImageTk.PhotoImage(file=r"C:\Users\Mr.MadX\KL\MadX_Player\Icon_and_img\p1.png")
#Pause Button
p2 = ImageTk.PhotoImage(file=r"C:\Users\Mr.MadX\KL\MadX_Player\Icon_and_img\p2.png")
#Forword Button
f1 = ImageTk.PhotoImage(file=r"C:\Users\Mr.MadX\KL\MadX_Player\Icon_and_img\f1.png")
#Backward Button
b1 = ImageTk.PhotoImage(file=r"C:\Users\Mr.MadX\KL\MadX_Player\Icon_and_img\r1.png")

#All buttons and slider
#--------------------------------------------
# Play Button
playbtn = Button(root,image=p1, command=playsong)
playwin = new_cnv.create_window(90,590, anchor="nw", window= playbtn)

#Pause Button
pausebtn = Button(root,image=p2, command= lambda: pause(paused))
pausewin = new_cnv.create_window(170,590, anchor="nw", window=pausebtn)

#Volume Slider
volslider =ttk.Scale(root, from_=1, to=0, orient='vertical', value=1, command=vol, length=90)
volsliderwin = new_cnv.create_window(350,570, anchor="nw", window= volslider)

#Forword Button
forrwordbtn = Button(root, image= f1 , command= forword)
forwordwin = new_cnv.create_window(250,590, anchor='nw', window= forrwordbtn)

#Backward Button
Backwardbtn = Button(root, image= b1, command= Backward)
Backwardwin =new_cnv.create_window(10,590, anchor="nw", window=Backwardbtn)

#Song Slider
songslider =ttk.Scale(root, from_=1, to=100, orient='horizontal', value=0, command=song_slider, length=360)
songsliderwin = new_cnv.create_window(20,520, anchor="nw", window= songslider)

#Creating song timing status bar 
song_timer = Label(root,text='00:00:00')
song_timer.place(x=20,y=495,)

#Creating song length status bar
song_full_time = Label(root,text='00:00:00')
song_full_time.place(x=330,y=495)

#Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# + Add song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add songs to playlist", command=add_song)

# delete songs form list
remove_song = Menu(my_menu)
my_menu.add_cascade(label="Delete Song", menu=remove_song)
remove_song.add_command(label="Delete one song for playlist", command=delete_song)
remove_song.add_command(label="Delete all song for playlist", command=delete_songs)

#Ending loop
mainloop()