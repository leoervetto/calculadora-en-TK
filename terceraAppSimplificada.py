import tkinter as tk

# Función para manejar los eventos de los botones
def escribir(numero):
    entrada.set(entrada.get() + str(numero))

def operar(operador):
    entrada.set(entrada.get() + operador)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.set(resultado)
    except:
        entrada.set("Error")

def limpiar():
    entrada.set("")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x600")

entrada = tk.StringVar()

# Pantalla de la calculadora
pantalla = tk.Entry(ventana, textvariable=entrada, font=('Arial', 18), bd=10, insertwidth=2, width=14, borderwidth=4)
pantalla.grid(row=0, column=0, columnspan=4)

# Botones numéricos
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
botones = []

for i, numero in enumerate(numeros, 1):
    botones.append(tk.Button(ventana, text=str(numero), padx=20, pady=20,
                             command=lambda numero=numero: escribir(numero)))
    botones[-1].grid(row=(i-1)//3+1, column=(i-1)%3)

# Botones de operación
boton_sumar = tk.Button(ventana, text="+", padx=20, pady=20, command=lambda: operar("+"))
boton_sumar.grid(row=1, column=3)
boton_restar = tk.Button(ventana, text="-", padx=20, pady=20, command=lambda: operar("-"))
boton_restar.grid(row=2, column=3)
boton_igual = tk.Button(ventana, text="=", padx=20, pady=20, command=calcular)
boton_igual.grid(row=4, column=3)
boton_limpiar = tk.Button(ventana, text="C", padx=20, pady=20, command=limpiar)
boton_limpiar.grid(row=4, column=0)

ventana.mainloop()