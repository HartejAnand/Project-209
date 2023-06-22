import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import time
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path


def openChatWindow():

    print("\n\t\t\t\tIP MESSENGER")

    #Client GUI starts here
    window=Tk()

    window.title('Messenger')
    window.geometry("500x350")

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    namelabel = Label(window, text= "Enter Your Name", font = ("Calibri",10))
    namelabel.place(x=10, y=8)

    name = Entry(window,width =30,font = ("Calibri",10))
    name.place(x=120,y=8)
    name.focus()

    separator = ttk.Separator(window, orient='horizontal')
    separator.place(x=0, y=35, relwidth=1, height=0.1)

    labelusers = Label(window, text= "Active Users", font = ("Calibri",10))
    labelusers.place(x=10, y=50)

    listbox = Listbox(window,height = 5,width = 67,activestyle = 'dotbox', font = ("Calibri",10))
    listbox.place(x=10, y=70)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    connectButton=Button(window,text="Connect",bd=1, font = ("Calibri",10))
    connectButton.place(x=282,y=160)

    disconnectButton=Button(window,text="Disconnect",bd=1, font = ("Calibri",10))
    disconnectButton.place(x=350,y=160)

    window.mainloop()

def play():
    global song_selected
    song_selected=listbox.get(ANCHOR)
    pygame
    mixer.init()
    mixer.music.load('shared_files'+song_selected)
    mixer.music.play()
    if(song_selected !=""):
        infoLabel.configure(text="Now playing " + song_selected)
    else:
        infoLabel.configure(text="")
    
def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")
    

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))


    openChatWindow()

setup()