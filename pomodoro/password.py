import json
import pyperclip
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

FONT_NAME = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# TODO PASSWORD GENERATOR
def generatorpassword():
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


# ---------------------------- FIND PASSWORD ------------------------------- #
# TODO FIND PASSWORD
def find_password():
    try:
        with open(r'C:\Users\Julio\Desktop\Pessoais\apps_desenvolvidos\senhas_cadastradas.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Oops', message=f'Nenhum arquivo foi encontrado!!!')
    else:
        website = web_entry.get()
        if website in data:
            messagebox.showinfo(title=f'website: {website}', message=f'Segue os dados de usuário:\n'
                                                                     f'Email/Username: {data[website]["email"]}\n'
                                                                     f'Password: {data[website]["password"]}')
        else:
            messagebox.showinfo(title='Oops', message=f'Não existe dado de usuário '
                                                      f'relacionado ao site: {website}')
    finally:
        web_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# TODO SAVE PASSWORD

def save():
    website = web_entry.get()
    email = email_entry.get()
    senha = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": senha,
        }
    }

    if website == '' or senha == '':
        messagebox.showinfo(title='Oops', message=f'Por favor!!!\nNão deixe nenhum campo em branco!!!')
    else:
        confirmation = messagebox.askokcancel(title='Cadastro', message=f'Deseja cadastrar os dados descritos abaixo:\n'
                                                                        f'Website: {website}\n'
                                                                        f'Email/Username: {email}\n'
                                                                        f'senha: {senha}')
        if confirmation:
            try:
                with open(r'C:\Users\Julio\Desktop\Pessoais\apps_desenvolvidos\senhas_cadastradas.json', 'r') \
                        as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open(r'C:\Users\Julio\Desktop\Pessoais\apps_desenvolvidos\senhas_cadastradas.json', 'w') \
                        as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                data.update(new_data)
                with open(r'C:\Users\Julio\Desktop\Pessoais\apps_desenvolvidos\senhas_cadastradas.json', 'w') \
                        as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                web_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo(title='Confirmação', message=f'Dados cadastrados com sucesso!!!')


# ---------------------------- UI SETUP ------------------------------- #
# TODO UI SETUP

window = Tk()
window.title('Password Manager')
window.config(padx=40, pady=40, bg='white')

canvas = Canvas(width=220, height=168)
canvas.config(bg='white', highlightthickness=0)
code_file = PhotoImage(file='password-manager-start/logo.png')
canvas.create_image(110, 84, image=code_file)
canvas.grid(row=0, column=1)

web_label = Label(text='Website:', fg='black', bg='white', font=(FONT_NAME, 10, 'bold'))
web_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:', fg='black', bg='white', font=(FONT_NAME, 10, 'bold'))
email_label.grid(row=2, column=0)
password_label = Label(text='Password:', fg='black', bg='white', font=(FONT_NAME, 10, 'bold'))
password_label.grid(row=3, column=0)

web_entry = Entry(window, bd=2, width=40)
web_entry.grid(row=1, column=1, columnspan=2, sticky=W)
web_entry.focus()

email_entry = Entry(window, bd=2, width=60)
email_entry.grid(row=2, column=1, columnspan=2, sticky=W)
email_entry.insert(0, 'juliofirminoreis@hotmail.com')

password_entry = Entry(window, bd=2, width=40)
password_entry.grid(row=3, column=1, columnspan=2, sticky=W)

generate_buttom = Button(text='Gerador senhas', width=15, command=generatorpassword)
generate_buttom.grid(row=3, column=2, sticky=SE, pady=5)

search_buttom = Button(text='Search', width=15, command=find_password)
search_buttom.grid(row=1, column=2, sticky=SE, pady=5)

add_buttom = Button(text='Register', width=34, command=save)
add_buttom.grid(row=5, column=1, columnspan=2, sticky=W, pady=2)

window.mainloop()
