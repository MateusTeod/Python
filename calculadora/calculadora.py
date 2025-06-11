from tkinter import *
from tkinter import ttk


#definindo a janela da calc
janela = Tk()
janela.title('Calculadora')
janela.geometry('400x355')
janela.minsize(400, 355)
janela.maxsize(400, 355)

numero1 = ''
divisao = FALSE
multiplica = FALSE
adicao = FALSE
subtracao = FALSE

#definindo a cor do fundo da calc
janela.configure(background='#282828')

#definindo layout da calc
e = Entry(janela, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#a7a28f', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)

#funcoes operadores
def botao_click(num):
    e.insert(END, num)
    
def botao_div():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = e.get()
    e.delete(0, END)
def botao_mult():
    global numero1
    global multiplica
    multiplica = TRUE
    numero1 = e.get()
    e.delete(0, END)
def botao_sub():
    global numero1
    global subtracao
    subtracao = TRUE
    numero1 = e.get()
    e.delete(0, END)
def botao_adicao():
    global numero1
    global adicao
    adicao = TRUE
    numero1 = e.get()
    e.delete(0, END)
def botao_porc():
    return
def botao_clear():
    e.delete(0, END)
    
def botao_igual():
    global subtracao
    global adicao
    global multiplica
    global divisao
    global numero1
    numero2 = e.get()
    e.delete(0, END)
    if adicao == TRUE:
        e.insert(0, str(int(numero1) + int(numero2)))
        adicao = FALSE
    elif subtracao == TRUE:
        e.insert(0, str(int(numero1) - int(numero2)))
        subtracao = FALSE
    elif multiplica == TRUE:
        e.insert(0, str(int(numero1) * int(numero2)))
        multiplica = FALSE
    elif divisao == TRUE:
        try:
            e.insert(0, str(int(numero1) / int(numero2)))
        except ZeroDivisionError:
            e.insert(0, "Erro")
        divisao = FALSE
        

#botao de divisao
divide = Button(janela, 
                text='÷',
                padx=40,
                pady=20,
                command=botao_div,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
divide.grid(row=0, column=4)
#primeira fileira 'num1'
um = Button(janela, 
                text='1',
                padx=40,
                pady=20,
                command=lambda: botao_click(1),
                fg='#FFFFFF',
                activeforeground='#240046',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
um.grid(row=1, column=1)

dois = Button(janela, 
                text='2',
                padx=40,
                pady=20,
                command=lambda: botao_click(2),
                fg='#FFFFFF',
                activeforeground='#240046',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
dois.grid(row=1, column=2)

tres = Button(janela, 
                text='3',
                padx=42,
                pady=20,
                command=lambda: botao_click(3),
                fg='#FFFFFF',
                activeforeground='#240046',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
tres.grid(row=1, column=3)

multiplica = Button(janela, 
                text='x',
                padx=42,
                pady=20,
                command= botao_mult,
                fg='#FFFFFF',
                activeforeground='#240046',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
multiplica.grid(row=1, column=4)

#segunda fileira
quatro = Button(janela, 
                text='4',
                padx=40,
                pady=20,
                command=lambda: botao_click(4),
                fg='#FFFFFF',
                activeforeground='#240046',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
quatro.grid(row=2, column=1)

cinco = Button(janela, 
                text='5',
                padx=40,
                pady=20,
                command=lambda: botao_click(5),
                fg='#FFFFFF',
                activeforeground='#240046',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
cinco.grid(row=2, column=2)

seis = Button(janela, 
                text='6',
                padx=42,
                pady=20,
                command=lambda: botao_click(6),
                fg='#FFFFFF',
                activeforeground='#240046',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
seis.grid(row=2, column=3)

menos = Button(janela, 
                text=' -',
                padx=42,
                pady=20,
                command= botao_sub,
                fg='#FFFFFF',
                activeforeground='#240046',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
menos.grid(row=2, column=4)

#terceira fileira
sete = Button(janela, 
                text='7',
                padx=40,
                pady=20,
                command=lambda: botao_click(7),
                fg='#FFFFFF',
                activeforeground='#240046',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
sete.grid(row=3, column=1)

oito = Button(janela, 
                text='8',
                padx=40,
                pady=20,
                command=lambda: botao_click(8),
                fg='#FFFFFF',
                activeforeground='#240046',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
oito.grid(row=3, column=2)

nove = Button(janela, 
                text='9',
                padx=42,
                pady=20,
                command=lambda: botao_click(9),
                fg='#FFFFFF',
                activeforeground='#240046',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
nove.grid(row=3, column=3)

adicao = Button(janela, 
                text='+',
                padx=42,
                pady=20,
                command= botao_adicao,
                fg='#FFFFFF',
                activeforeground='#240046',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
adicao.grid(row=3, column=4)

#quarta fileira
zero = Button(janela, 
                text='0',
                padx=91,
                pady=20,
                command=lambda: botao_click(0),
                fg='#FFFFFF',
                activeforeground='#240046',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
zero.grid(row=4, column=1, columnspan=2)

limpa = Button(janela, 
                text='C',
                padx=41,
                pady=20,
                command= botao_clear,
                fg='#FFFFFF',
                activeforeground='#240046',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
limpa.grid(row=4, column=3)

igual = Button(janela, 
                text='=',
                padx=42,
                pady=20,
                command= botao_igual,
                fg='#FFFFFF',
                activeforeground='#240046',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
igual.grid(row=4, column=4)



#funcao para nao fechar a janela
janela.mainloop()