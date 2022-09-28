from cProfile import label
from email.mime import image
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

def add_song():
    song = filedialog.askopenfilename(initialdir=r'C:\Users\Mr.MadX\Desktop\Madx', title="ChooseA Song", filetypes=(("mp3 file","*mp3"), ))
    song = song.replace("C:/Users/Mr.MadX/Desktop/Madx/", "")
    song = song.replace(".mp3","")

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

#Pause function

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

#Resume function

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()

#Stop function

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()
    playlist.select_clear(ACTIVE)

#Volume control function

def vol(x):
    pygame.mixer.music.set_volume(volslider.get())


root = Tk()
root.title("MadX Player")
root.geometry()

mixer.init()
songstatus = StringVar()
songstatus.set("Choosing")

#Define icon and images
p1 = PhotoImage(file=r"C:\Users\Mr.MadX\Desktop\icon\p1.png")
p2 = PhotoImage(file=r"C:\Users\Mr.MadX\Desktop\icon\p2.png")
r1 = PhotoImage(file=r"C:\Users\Mr.MadX\Desktop\icon\r1.png")
s1 = PhotoImage(file=r"C:\Users\Mr.MadX\Desktop\icon\s1.png")

#Play List------------------------

playlist = Listbox(root,selectmode=SINGLE,bg='black',fg='green', selectbackground='gray', selectforeground= 'blue',font=('Comic Sans MS',17),width=40)
playlist.pack(pady=20)

# os.chdir(r'C:\Users\Mr.MadX\Desktop\Madx')
# songs = os.listdir()
# for s in songs:
#     playlist.insert(END,s)

#All frames
ftframe = Frame(root)
ftframe.pack()

volframe = LabelFrame(ftframe,text='Vol')
volframe.grid(row=1,column=4,padx=10) 


playbtn = Button(ftframe,image = p1, borderwidth=0, command=playsong)
playbtn.grid(row=1,column=0,padx=5)

pausebtn = Button(ftframe,image=p2, borderwidth=0, command=pausesong)
pausebtn.grid(row=1,column=1,padx=5)

resumebtn = Button(ftframe,image=r1, borderwidth=0, command=resumesong)
resumebtn.grid(row=1,column=2,padx=5)

stopbtn = Button(ftframe,image=s1, borderwidth=0, command=stopsong)
stopbtn.grid(row=1,column=3)

volslider =ttk.Scale(volframe, from_=1, to=0, orient='vertical', value=1, command=vol, length=100)
volslider.pack(padx=2)

# create status bar 
status_bar = Label(root,text='',bd=1, relief=GROOVE, anchor=SE)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

#Create menu
my_menu =Menu(root)
root.config(menu=my_menu)

#+ Add song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add one song to playlist", command=add_song)


mainloop()