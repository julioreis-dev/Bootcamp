from tkinter import *
from tkinter import messagebox
import pyperclip
from random import choice, randint, shuffle

FONT_NAME = "Arial"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# TODO PASSWORD GENERATOR
def newpassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    final_password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, final_password)
    pyperclip.copy(final_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# TODO SAVE PASSWORD

def save():
    website = web_entry.get()
    email = email_entry.get()
    senha = password_entry.get()

    if website == '' or senha == '':
        messagebox.showinfo(title='Oops', message=f'Por favor!!!\nNão deixe nenhum dado em branco!!!')
    else:
        confirmation = messagebox.askokcancel(title='Aviso ao usuário', message=f'Esses são os dados que '
                                                                                f'deverão cadastrados:\n'
                                                                                f'Website: {website}\n'
                                                                                f'Email: {email}\n'
                                                                                f'Senha: {senha}\n'
                                                                                f'Deseja confirmar o cadastro?')
        if confirmation:
            with open(r'C:\Users\Julio\Desktop\Pessoais\apps_desenvolvidos\senhas_cadastradas.txt', 'a') as data_file:
                data_file.write(f'{website} / {email} / {senha}\n')
                web_entry.delete(0, END)
                password_entry.delete(0, END)
            messagebox.showinfo(title='Confirmação', message=f'Dados cadastrados com sucesso!!!')


# ---------------------------- UI SETUP ------------------------------- #
# TODO UI SETUP

window = Tk()
window.title('Password Manager')
window.config(padx=100, pady=100, bg='white')

canvas = Canvas(width=140, height=168)
canvas.config(bg='white', highlightthickness=0)
code_file = PhotoImage(file='password-manager-start/logo.png')
canvas.create_image(70, 84, image=code_file)
canvas.grid(row=0, column=1)

web_label = Label(text='Website:', fg='black', bg='white', font=(FONT_NAME, 10, 'bold'))
web_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:', fg='black', bg='white', font=(FONT_NAME, 10, 'bold'))
email_label.grid(row=2, column=0)
password_label = Label(text='Password:', fg='black', bg='white', font=(FONT_NAME, 10, 'bold'))
password_label.grid(row=3, column=0)

web_entry = Entry(window, bd=1, width=36)
web_entry.grid(row=1, column=1, columnspan=2, sticky=W)
web_entry.focus()

email_entry = Entry(window, bd=1, width=36)
email_entry.grid(row=2, column=1, columnspan=2, sticky=W)
email_entry.insert(0, 'juliofirminoreis@hotmail.com')

password_entry = Entry(window, bd=1, width=36)
password_entry.grid(row=3, column=1, columnspan=2, sticky=W)

generate_buttom = Button(text='Gerador senhas', width=30, command=newpassword)
generate_buttom.grid(row=4, column=1, sticky=SE)

add_buttom = Button(text='Register', width=30, command=save)
add_buttom.grid(row=5, column=1, columnspan=2, sticky=W)

window.mainloop()
