from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1#25
SHORT_BREAK_MIN = 0.1#5
LONG_BREAK_MIN = 0.1#20
reps = 0
new_checkmark = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, new_checkmark
    reps = 0
    new_checkmark = ""
    checkmark.config(text="")
    label.config(text="New Timer", fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    if reps==9:
        window.focus_force()
        count_down(LONG_BREAK_MIN * 60)
        label.config(text="Long Break", fg=RED)
    elif reps%2==0:
        window.focus_force()
        count_down(WORK_MIN*60)
        label.config(text="Work", fg=GREEN)
    else:
        window.focus_force()
        count_down(SHORT_BREAK_MIN*60)
        label.config(text="Short Break", fg=PINK)

    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    import math
    minutes = str(math.floor(count / 60))
    if len(minutes)==1:
        minutes = minutes.zfill(2)

    seconds = str(count%60)
    if len(seconds)==1:
        seconds = seconds.zfill(2)
    canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        global reps, new_checkmark
        if reps<=9:
            start_timer()
            if reps%2==1:
                new_checkmark += "✓"
                checkmark.config(text=new_checkmark,  fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro-Timer")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer")
label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
label.grid(row=0, column=1)

checkmark = Label()
checkmark.grid(row=4, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

l_button = Button()
l_button.config(text="start", command=start_timer)
l_button.grid(row=3, column=0)
r_button = Button()
r_button.config(text="reset", command=reset_timer)
r_button.grid(row=3, column=3)

window.mainloop()