from tkinter import *
import pandas as pd
import random

current_card = {}
def wordchosen():
    global current_card, temptime
    window.after_cancel(temptime)
    current_card = random.choice(learnlist)
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(card_word, text=current_card['French'])
    canvas.itemconfig(card_background, image=card_front_img)
    temptime = window.after(3000, func=changechosen)


def changechosen():
    canvas.itemconfig(card_title, text='Portugues')
    canvas.itemconfig(card_word, text=current_card['Portugues'])
    canvas.itemconfig(card_background, image=card_back_img)


def studedword():
    learnlist.remove(current_card)
    datas = pd.DataFrame(learnlist)
    datas.to_csv('flash-card-project-start/data/words_to_learn.csv', index=False)
    wordchosen()


try:
    data = pd.read_csv('flash-card-project-start/data/words_to_learn.csv')
except FileNotFoundError:
    original = pd.read_csv('flash-card-project-start/data/french_words.csv')
    learnlist = original.to_dict(orient='records')
else:
    learnlist = data.to_dict(orient='records')

BACKG = '#B1DDC6'
# construindo janela TKinter
window = Tk()
window.title('flash_card')
window.config(padx=50, pady=50, bg=BACKG)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='flash-card-project-start/images/card_front.png')
card_back_img = PhotoImage(file='flash-card-project-start/images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 265, text='', font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKG, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# tratamento dos botões de erro
wrong_image = PhotoImage(file='flash-card-project-start/images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wordchosen)
wrong_button.grid(row=1, column=0)

# tratamento dos botões de acerto
check_image = PhotoImage(file='flash-card-project-start/images/right.png')
check_button = Button(image=check_image, highlightthickness=0, command=studedword)
check_button.grid(row=1, column=1)
temptime = window.after(3000, func=changechosen)
wordchosen()
window.mainloop()
