from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
# TODO CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
# TODO TIMER RESET
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    check_label.config(text='')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
# TODO TIMER MECHANISM
def start_timer():
    global reps
    reps += 1
    work_time_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    work_time = [1, 3, 5, 7]
    break_time = [2, 4, 6]

    if reps in work_time:
        count_down(work_time_sec)
        timer_label.config(text='Work', fg=GREEN)

    elif reps in break_time:
        count_down(short_break_sec)
        timer_label.config(text='Break', fg=PINK)

    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text='Break', fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# TODO COUNTDOWN MECHANISM
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += '✔'
        check_label.config(text=marks, fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
# TODO UI SETUP
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=201, height=225)
canvas.config(bg=YELLOW, highlightthickness=0)
tomato_file = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_file)
timer_text = canvas.create_text(103, 130, text='00:00', font=(FONT_NAME, 26, 'bold'), fill='white')
canvas.grid(row=1, column=1)

timer_label = Label(text='Timer',
                    fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, 'bold'))
timer_label.grid(row=0, column=1)

start_buttom = Button(text='Start', font=('Arial', 12, 'bold'), command=start_timer)
start_buttom.grid(row=2, column=0)

reset_buttom = Button(text='Reset', font=('Arial', 12, 'bold'), command=reset_timer)
reset_buttom.grid(row=2, column=2)

check_label = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
check_label.grid(row=3, column=1)

window.mainloop()
