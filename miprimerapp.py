
import tkinter as tk



def Sumar():
    numero1 = numeroIngreso.get()
    numero2 = numeroIngreso2.get()
    Resultado = int(numero1) + int(numero2)
    resultadoMostrado.config(text=Resultado)    
    

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x600")

numero1 = tk.Label(ventana, text="Ingrese el primer numero")
numero1.pack()
numeroIngreso = tk.Entry(ventana)
numeroIngreso.pack()
numeroIngreso2 = tk.Entry(ventana)
numeroIngreso2.pack()
botonSumar = tk.Button(ventana, text="Sumar", command=Sumar)
botonSumar.pack()
resultadoMostrado = tk.Label(ventana, text="aqui se ve el resultado")
resultadoMostrado.pack()






ventana.mainloop()