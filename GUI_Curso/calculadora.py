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

operacion=""
reset_pantalla=False
resultado=0

############################Pantalla########################

numeroPantalla=StringVar()

cuadroPantalla=Entry(miFrame, textvariable=numeroPantalla)
cuadroPantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
cuadroPantalla.config(bg="black", fg="orange", justify="right")

##########################Pulsaciones teclado####################

def numeroPulsado(num):
    
    global operacion
    global reset_pantalla
    if reset_pantalla!=False:
        numeroPantalla.set(num)
        reset_pantalla=False        
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

##########################Funcion suma###########################

def suma(num):   
    global operacion
    global resultado
    global reset_pantalla
    
    resultado+=int(num)
    operacion="suma"
    reset_pantalla=True
    
    numeroPantalla.set(resultado)
    
###########################FUncion resta########################

num1=0

contador_resta=0
    
def resta(num):   
    global operacion
    global resultado
    global num1
    global contador_resta
    global reset_pantalla
    
    if contador_resta==0:
        num1=int(num)
        resultado=num1
    else:
        if contador_resta==1:
            resultado=num1-int(num)
        else:
            resultado=int(resultado)-int(num)
        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()
        
    contador_resta=contador_resta+1
    reset_pantalla=True
    operacion="resta"
    
    
###########################FUncion el_resultado#################
def el_resultado():
    global resultado
    global contador_resta
    global contador_multi
    global contador_div
    
    if operacion=="suma" :    
        numeroPantalla.set(resultado+int(numeroPantalla.get()))
        resultado=0 
        
    if operacion=="resta":
        numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))
        resultado=0
        contador_resta=0
        
    if operacion=="multiplicacion":
        numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))
        resultado=0
        contador_multi=0
    
    if operacion=="division" :
        numeroPantalla.set(int(resultado)/float(numeroPantalla.get()))
        resultado=0
        contador_div=0



##########################FUncion multiplicacion###################
    
contador_multi=0
def multiplicacion(num):
    global operacion
    global resultado
    global num1
    global reset_pantalla
    global contador_multi
    
    if contador_multi==0:
        num1=int(num)
        resultado=num1
    else:
        if contador_multi==1:
            resultado=num1*int(num)
        else:
            resultado=int(resultado)*int(num)
        
        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()
    contador_multi=contador_multi+1
    operacion="multiplicacion"
    reset_pantalla=True

###########################Funcion division####################
contador_div=0
def division(num):
    global operacion
    global resultado
    global num1
    global contador_div
    global reset_pantalla
    
    if contador_div==0:
        num1=float(num)
        resultado=num1
    else:
        if contador_div==1:
            resultado=num1/float(num)
        else:
            resultado=float(resultado)/float(num)
        
        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()
    contador_div=contador_div+1
    operacion="division"
    reset_pantalla=True
    
##########################FUncion reset#########################

def reset():
    global resultado
    resultado=0
    numeroPantalla.set("")
##########################Fila1#################################

boton7=Button(miFrame, text="7", width="3",command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)

boton8=Button(miFrame, text="8", width="3", command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)

boton9=Button(miFrame, text="9", width="3", command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)

botondiv=Button(miFrame, text="/", width="3", command=lambda:division(numeroPantalla.get()))
botondiv.grid(row=2, column=4)

##########################Fila2##############################

boton4=Button(miFrame, text="4", width="3", command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)

boton5=Button(miFrame, text="5", width="3", command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)

boton6=Button(miFrame, text="6", width="3", command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)

botonmult=Button(miFrame, text="*", width="3", command=lambda:multiplicacion(numeroPantalla.get()))
botonmult.grid(row=3, column=4)

##########################Fila3##############################

boton1=Button(miFrame, text="1", width="3", command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)

boton2=Button(miFrame, text="2", width="3", command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)

boton3=Button(miFrame, text="3", width="3", command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)

botonres=Button(miFrame, text="-", width="3", command=lambda:resta(numeroPantalla.get()))
botonres.grid(row=4, column=4)

##########################Fila4##############################

boton0=Button(miFrame, text="0", width="3", command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=2)

botoncoma=Button(miFrame, text=",", width="3", command=lambda:numeroPulsado(","))
botoncoma.grid(row=5, column=3)

botonCE=Button(miFrame, text="CE", width="3", command=lambda:reset())
botonCE.grid(row=5, column=1)

botonsum=Button(miFrame, text="+", width="3", command=lambda:suma(numeroPantalla.get()))
botonsum.grid(row=5, column=4)

######################FIla5####################################

botonigual=Button(miFrame, text="=", width="10", command=lambda:el_resultado())
botonigual.grid(row=6, column=1, columnspan=4)
botonigual.config(justify="center")

raiz.mainloop()