#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 13:07:06 2021

@author: josemcr
"""


from tkinter import *

raiz= Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

######################################################################

minombre=StringVar()

######################################################################

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=5, pady=5)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=5, pady=5)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=5, pady=5)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=5, pady=5)

#######################################################################

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, padx=5, pady=5)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4, column=1, pady=5, sticky="nse")
textoComentario.config(yscrollcommand=scrollVert.set)

#######################################################################

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=5, pady=5)

passLabel=Label(miFrame, text="Contraseña:")
passLabel.grid(row=1, column=0, sticky="e", padx=5, pady=5)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=5, pady=5)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=5, pady=5)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=5, pady=5)

#######################################################################

def codigoBoton():
    minombre.set("Jose")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()



raiz.mainloop()