#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 00:00:36 2021

@author: josemcr
"""

from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)
miFrame.pack()

miLabel= Label(miFrame, text="Hola mundo", fg="blue", font=("Comic Sans MS",18))
miLabel.place(x=100, y=200)
#Label().place()

root.mainloop()