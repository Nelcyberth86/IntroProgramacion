import tkinter as tk
from tkinter import *

def limpiarCampos():
    NA.set(0)
    NB.set(0)

def sumar():
    numeroA=NA.get()
    numeroB=NB.get()
    numeroR=numeroA+numeroB
    NR.set(numeroR)
    limpiarCampos()

def resta():
        numeroA = NA.get()
        numeroB = NB.get()
        numeroR = numeroA - numeroB
        NR.set(numeroR)
        limpiarCampos()

def dividir():
    numeroA=NA.get()
    numeroB=NB.get()
    numeroR=numeroA / numeroB
    NR.set(numeroR)
    limpiarCampos()

def multiplicar():
    numeroA=NA.get()
    numeroB=NB.get()
    numeroR=numeroA * numeroB
    NR.set(numeroR)
    limpiarCampos()


ventana=tk.Tk()
ventana.config(width=300,height=200)

etiquetaNA=Label(ventana,text="Número A:")
etiquetaNA.place(x=0,y=0)

NA=IntVar()
entradaNA=Entry(ventana,textvariable=NA)
entradaNA.place(x=70,y=0)



etiquetaNB=Label(ventana,text="Número B:")
etiquetaNB.place(x=0,y=30)

NB=IntVar()
entradaNB=Entry(ventana,textvariable=NB)
entradaNB.place(x=70,y=30)


etiquetaRES=Label(ventana,text="Resultado:")
etiquetaRES.place(x=0,y=60)

NR=IntVar()
salidaRES=Entry(ventana,textvariable=NR)
salidaRES.place(x=70,y=60)

botonTransportar=Button(ventana,text="Sumar A y B", command=sumar)
botonTransportar.place(x=0,y=90)

botonTransportar=Button(ventana,text="resta A y B", command=resta)
botonTransportar.place(x=0,y=120)

botonTransportar=Button(ventana,text="multiplicar A y B", command=multiplicar)
botonTransportar.place(x=0,y=150)

botonTransportar=Button(ventana,text="dividir A y B", command=dividir)
botonTransportar.place(x=0,y=180)




ventana.mainloop()