#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 2021

@author: josemcr
"""

from tkinter import *

# Crear la ventana principal o raiz
raiz=Tk()
raiz.title("Ventana de pruebas")
raiz.resizable(1, 1)                     #Dos boolean, el primero indica el ancho y el segundo el alto
#raiz.geometry("650x350")                Hay que darle el tamaño al frame, no a la raiz
#raiz.iconbitmap("chess.ico")
raiz.config(bg="black")

# Crear un frame
miFrame = Frame()
miFrame.pack(side="right", anchor="n")   #side(left,right,top,botton), anchor(n,s,e,w), fill(x,y -> expand="True",none, both)
miFrame.config(bg="gray")
miFrame.config(width="650", height="350")
miFrame.config(bd=35)
miFrame.config(relief="groove")         
miFrame.config(cursor="hand2")


raiz.mainloop()


