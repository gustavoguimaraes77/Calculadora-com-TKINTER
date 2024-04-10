# INTERFACE GRÁFICA BÁSICA DE UMA CALCULADORA COM O USO DO TKINTER

import tkinter as tk


def somar():
    number1 = float(entry1.get())
    number2 = float(entry2.get())
    Resultado = number1 + number2
    result.config(text=f'Total:%d'% (Resultado))

def subtrair():
    number1 = float(entry1.get())
    number2 = float(entry2.get())
    subtracao = number1 - number2
    result.config(text=f'Total:%d'% (subtracao))

def multip():
    number1 = float(entry1.get())
    number2 = float(entry2.get())
    multiplicacao = number1 * number2
    result.config(text=f'Total:%d'% (multiplicacao))

def div():
    number1 = float(entry1.get())
    number2 = float(entry1.get())
    divisao = number1 / number2
    result.config(text=f'Total:%d'% (divisao))

root = tk.Tk()
root.title('CALCULADORA')
root.geometry('300x410')

label1 = tk.Label(root, text='1º número:')
label1.pack()

entry1 = tk.Entry(root, bg='yellow')
entry1.pack()

# --------------

label2 = tk.Label(root, text='2º número:')
label2.pack()

entry2 = tk.Entry(root, bg='yellow')
entry2.pack()
 
 #--------------

label3 = tk.Label(root, text=' ')
label3.pack()

btn_soma = tk.Button(root, text='Soma', width = 20, fg='white', bg='#000000', command = somar)
btn_soma.pack()

label4 = tk.Label(root, text=' ')
label4.pack()

btn_sub = tk.Button(root, text='Subtração', width = 20, fg='white', bg='#000000', command = subtrair)
btn_sub.pack()

label5 = tk.Label(root, text=' ')
label5.pack()

btn_multi = tk.Button(root, text='Multiplicação', width = 20, fg='white', bg='#000000', command = multip)
btn_multi.pack()

label6 = tk.Label(root, text=' ')
label6.pack()

btn_div = tk.Button(root, text='Divisão', width = 20, fg='white', bg='#000000', command = div)
btn_div.pack()

label7 = tk.Label(root, text=' ')
label7.pack()

result = tk.Label(root, text='Resultado:')
result.pack()

root.mainloop()
