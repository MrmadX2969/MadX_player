from cProfile import label
from email.mime import image
from math import fabs
from tkinter import ttk
import pygame
from pygame import mixer
from tkinter import *
import os
import time
from mutagen.mp3 import MP3
from tkinter import filedialog

#Current time duration function

def song_duration():
    current_time =pygame.mixer.music.get_pos() / 1000

    #Song duration to time
    converte_song_time = time.strftime('%H:%M:%S', time.gmtime(current_time))

    status_bar.config(text=converte_song_time)
 
    status_bar.after(1000, song_duration)

# Add manny songs to the playlist
def add_song():
    song = filedialog.askopenfilenames(initialdir=r'C:\Users\Mr.MadX\Desktop\Madx', title="ChooseA Song", filetypes=(("mp3 file","*mp3"), ))
#Creating for loop to add multiple songs in one time
    for song in song:
        song = song.replace("C:/", "")
        song = song.replace(".mp3","")
#Insert songs in playlist
        playlist.insert(END, song)

#Play function

def playsong():
    song = playlist.get(ACTIVE)
    song = f'C:/Users/Mr.MadX/Desktop/Madx/{song}.mp3'
    print(song)
    mixer.music.load(song)
    songstatus.set("Playang")
    mixer.music.play()

    song_duration()

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
  
#Stop function

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()
    playlist.select_clear(ACTIVE)

#Volume control function

def vol(x):
    mixer.music.set_volume(volslider.get())


#All frames

#Root frame
root = Tk()
root.title("MadX Player")
root.geometry()

#Play List Layout

playlist = Listbox(root,selectmode=SINGLE,bg='black',fg='green', selectbackground='gray', selectforeground= 'blue',font=('Comic Sans MS',17),width=40)
playlist.pack(pady=20)

#Button frame
button_frm = Frame(root)
button_frm.pack()

#Volume outline frame
volframe = LabelFrame(button_frm,text='Vol')
volframe.grid(row=1,column=4,padx=10)

mixer.init()
songstatus = StringVar()
songstatus.set("Choosing")



#Define icon and images
p1 = PhotoImage(file=r"C:\Users\Mr.MadX\Desktop\icon\p1.png")
p2 = PhotoImage(file=r"C:\Users\Mr.MadX\Desktop\icon\p2.png")
s1 = PhotoImage(file=r"C:\Users\Mr.MadX\Desktop\icon\s1.png")

#All buttons

playbtn = Button(button_frm,image = p1, borderwidth=0, command=playsong)
playbtn.grid(row=1,column=0,padx=5)

pausebtn = Button(button_frm,image=p2, borderwidth=0, command= lambda: pause(paused))
pausebtn.grid(row=1,column=1,padx=5)

stopbtn = Button(button_frm,image=s1, borderwidth=0, command=stopsong)
stopbtn.grid(row=1,column=3)

volslider =ttk.Scale(volframe, from_=1, to=0, orient='vertical', value=0.5, command=vol, length=100)
volslider.pack(padx=2)

#Creating song timing status bar 
status_bar = Label(root,text='',bd=1, relief=GROOVE, anchor=SE)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

#Create menu
my_menu =Menu(root)
root.config(menu=my_menu)

# + Add song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add songs to playlist", command=add_song)


mainloop()