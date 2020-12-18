from tkinter import *
import time

def ShowChoice():
    print(opt.get())

def add(*args):
    sum = 0
    for n in args:
        sum = sum + n
    cav.itemconfig(result, text=sum)


def clean():
    cav.itemconfig(result, text='')


BLUE = '#04d8fb'
GREEN = '#a8dda8'
t = time.localtime()
window = Tk()
window.title(f'Sistema de gerenciamento de contratos marítimos {t[0]} - CMAR')
window.minsize(width=600, height=450)
window.config(padx=5, pady=5, bg=GREEN)

canvas = Canvas(width=245, height=110, bg=GREEN, highlightthickness=0)
petro = PhotoImage(file='logo.png')
canvas.create_image(125, 55, image=petro)
canvas.grid(row=0, column=1, padx=5, pady=5)

cav = Canvas(width=300, height=100, bg=GREEN, highlightthickness=0)
result = cav.create_text(150, 50, text='', font=('Ariel', 10, 'bold'))
cav.grid(row=7, column=1, padx=0, pady=0)

# Label
my_label = Label(text=f'Planilha Guia de Medição',
                 fg='black', bg=GREEN, font=('Arial', 15, 'italic'))
my_label.grid(row=1, column=1, padx=15, pady=15)

version_label = Label(text='Versão',
                 fg='black', bg=GREEN, font=('Arial', 15, 'bold'))
version_label.grid(row=2, column=1, padx=5, pady=5)

med_label = Label(text='Escolha o mês:',
                 fg='black', bg=GREEN, font=('Arial', 12, 'bold'))
med_label.grid(row=2, column=2, padx=5, pady=5)

# botão
previa_buttom = Button(text='Emitir prévia', font=('Arial', 12, 'bold'), padx=17, pady=0)
previa_buttom['command'] = lambda: add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
previa_buttom.grid(row=3, column=0)

inoper_buttom = Button(text='Indisp', font=('Arial', 12, 'bold'), padx=40, pady=0, command=clean)
inoper_buttom.grid(row=4, column=0, padx=5, pady=5)

calcular_buttom = Button(text='Versão final', font=('Arial', 12, 'bold'), padx=20, pady=0)
calcular_buttom.grid(row=5, column=0)

email_buttom = Button(text='Enviar email', font=('Arial', 12, 'bold'), padx=18, pady=0)
email_buttom.grid(row=6, column=0, padx=5, pady=5)

opt = IntVar()
opt.set(1)
month = [("Janeiro", 1), ("Fevereiro", 2), ("Março", 3), ("Abril", 4), ("Maio", 5), ('Junho', 6), ('Julho', 7),
         ('Agosto', 8), ('Setembro', 9), ('Outubro', 10), ('Novembro', 11), ('Dezembro', 12)]
incr=0
for mt, val in month:
    Radiobutton(window,
                text=mt,
                padx=20,
                variable=opt,
                bg=GREEN,
                font=('Arial', 10, 'bold'),
                command=ShowChoice,
                value=val).place(x=450, y=210+incr)
    incr+=20

version = Spinbox(window, from_=0, to=10, width=5, font=('Arial', 14, 'bold'), bg=GREEN)
version.grid(row=3, column=1)

window.mainloop()
