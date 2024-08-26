from cgitb import text
import tkinter as tk
from turtle import clear







def Escribe1():
           Entrada1.set(Entrada1.get() + "1")
           
def Escribe2():
           Entrada1.set(Entrada1.get() + "2")

def Escribe3():
           Entrada1.set(Entrada1.get() + "3")
           
def Escribe4():
           Entrada1.set(Entrada1.get() + "4")

def Escribe5():
           Entrada1.set(Entrada1.get() + "5")
           
def Escribe6():
           Entrada1.set(Entrada1.get() + "6")

def Escribe7():
           Entrada1.set(Entrada1.get() + "7")
           
def Escribe8():
           Entrada1.set(Entrada1.get() + "8")      

def Escribe9():
           Entrada1.set(Entrada1.get() + "9")  


def Sumar():
        Entrada1.set(Entrada1.get() + "+")

def igual():
        Resultado = eval(Entrada1.get())
        Entrada1.set(Resultado)

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x600")

Entrada1 = tk.StringVar()
PrimerNumero = tk.StringVar()

textouno = tk.Label(ventana, textvariable=Entrada1)
textouno.grid(row=1, column=1, columnspan=4)
pantalla = tk.Entry(ventana, textvariable=Entrada1)
pantalla.grid(row=1, column=1, columnspan=3, pady=10)
numero1 = tk.Button(ventana, text="1", command=Escribe1)
numero1.grid(row=2, column=1, sticky="nsew")
numero2 = tk.Button(ventana, text="2", command=Escribe2)
numero2.grid(row=2, column=2, sticky="nsew")
numero3 = tk.Button(ventana, text="3", command=Escribe3)
numero3.grid(row=2, column=3, sticky="nsew")
numero4 = tk.Button(ventana, text="4", command=Escribe4)
numero4.grid(row=3, column=1, sticky="nsew")
numero5 = tk.Button(ventana, text="5", command=Escribe5)
numero5.grid(row=3, column=2, sticky="nsew")
numero6 = tk.Button(ventana, text="6", command=Escribe6)
numero6.grid(row=3, column=3, sticky="nsew")
numero7 = tk.Button(ventana, text="7", command=Escribe7)
numero7.grid(row=4, column=1, sticky="nsew")
numero8 = tk.Button(ventana, text="8", command=Escribe8)
numero8.grid(row=4, column=2, sticky="nsew")
numero9 = tk.Button(ventana, text="9", command=Escribe9)
numero9.grid(row=4, column=3, sticky="nsew")
botonsuma = tk.Button(ventana, text="+", command=Sumar)
botonsuma.grid(row=2, column=4, sticky="nsew")
botonigual = tk.Button(ventana, text="=", command=igual)
botonigual.grid(row=4, column=4, sticky="nsew")








ventana.mainloop()

