#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 14:02:37 2021

@author: josemcr
"""

from tkinter import *

raiz= Tk()


miFrame=Frame(raiz)
miFrame.config(bg="gray")
miFrame.pack()

############################Pantalla########################

cuadroPantalla=Entry(miFrame)
cuadroPantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
cuadroPantalla.config(bg="black", fg="orange", justify="right")

##########################Fila1##############################

boton7=Button(miFrame, text="7", width="3")
boton7.grid(row=2, column=1)

boton8=Button(miFrame, text="8", width="3")
boton8.grid(row=2, column=2)

boton9=Button(miFrame, text="9", width="3")
boton9.grid(row=2, column=3)

botondiv=Button(miFrame, text="/", width="3")
botondiv.grid(row=2, column=4)

##########################Fila2##############################

boton4=Button(miFrame, text="4", width="3")
boton4.grid(row=3, column=1)

boton5=Button(miFrame, text="5", width="3")
boton5.grid(row=3, column=2)

boton6=Button(miFrame, text="6", width="3")
boton6.grid(row=3, column=3)

botonmult=Button(miFrame, text="*", width="3")
botonmult.grid(row=3, column=4)

##########################Fila3##############################

boton1=Button(miFrame, text="1", width="3")
boton1.grid(row=4, column=1)

boton2=Button(miFrame, text="2", width="3")
boton2.grid(row=4, column=2)

boton3=Button(miFrame, text="3", width="3")
boton3.grid(row=4, column=3)

botonres=Button(miFrame, text="-", width="3")
botonres.grid(row=4, column=4)

##########################Fila4##############################

boton0=Button(miFrame, text="0", width="3")
boton0.grid(row=5, column=2)

botoncoma=Button(miFrame, text=",", width="3")
botoncoma.grid(row=5, column=1)

botonigual=Button(miFrame, text="=", width="3")
botonigual.grid(row=5, column=3)

botonsum=Button(miFrame, text="+", width="3")
botonsum.grid(row=5, column=4)


raiz.mainloop()