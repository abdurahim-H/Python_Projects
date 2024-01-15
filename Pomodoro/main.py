# from tkinter import *
# import math
# # ---------------------------- CONSTANTS ------------------------------- #
# PINK = "#e2979c"
# RED = "#e7305b"
# GREEN = "#9bdeac"
# YELLOW = "#f7f5dd"
# FONT_NAME = "Courier"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
# reps = 0
# timer = None
# # ---------------------------- TIMER RESET ------------------------------- #
# def reset():
#     # my_label_2.grid_forget()
#     window.after_cancel(timer)
#     canvas.itemconfig(timer_text, text="00:00")
#     my_label.config(text="Timer")
#     my_label_2.config(text="")
#     global reps
#     reps = 0


# # ---------------------------- TIMER MECHANISM ------------------------------- # 
# def start_time():
#     global reps
#     reps = reps + 1
#     work_sec = WORK_MIN * 60
#     short_break_sec = SHORT_BREAK_MIN * 60
#     long_break_sec = LONG_BREAK_MIN * 60
#     if reps % 2 == 0:
#         count_down(short_break_sec)
#         my_label.config(text="Short Break", fg=RED)
#     elif reps % 8 == 0:
#         count_down(long_break_sec)
#         my_label.config(font="Long Break", fg=PINK)
#     else:
#         count_down(work_sec)
#         my_label.config(text="Working", fg=GREEN)


# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# def count_down(count):
#     minutes = math.floor(count / 60)
#     seconds = count % 60
#     if seconds < 10:
#         seconds = f"0{seconds}"

#     canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
#     # mins, secs = divmod(count, 60)
#     # canvas.itemconfig(timer_text, text=f"{mins}:{secs:02d}")
#     if count > 0:
#         global timer
#         timer = window.after(1000, count_down, count - 1)
#     else:
#         start_time()
#         marks = ""
#         for _ in range(math.floor(reps/2)):
#             marks += "✔"
#             my_label_2.config(text=marks)


# # ---------------------------- UI SETUP ------------------------------- #
# window = Tk()
# window.title("Pomodoro")
# window.config(padx=100, pady=50, bg=YELLOW)

# canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# tomato_imp = PhotoImage(file="tomato.png")
# canvas.create_image(100, 112, image=tomato_imp)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.grid(row=1, column=1)

# my_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW, highlightthickness=0)
# my_label.grid(row=0, column=1)

# button_1 = Button(text="Start", highlightthickness=0, command=start_time)
# button_1.grid(row=2, column=0)

# button_2 = Button(text="Reset", highlightthickness=0, command=reset)
# button_2.grid(row=2, column=2)

# my_label_2 = Label(bg=YELLOW, fg=GREEN, highlightthickness=0)
# my_label_2.grid(row=3, column=1)

# window.mainloop()


from tkinter import *
import math
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.20
SHORT_BREAK_MIN = 0.20
LONG_BREAK_MIN = 20
work_sessions = 0
reps = 0
timer = None
marks = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
	window.after_cancel(timer)
	canvas.itemconfig(timer_text, text="00:00")
	my_label.config(text="Timer")
	my_label_1.config(text="")
	global reps
	reps = 0

# Global variables
reps = 0
timer = None
marks = ""

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_work_time():
	global reps
	global timer
	global work_sessions
	if timer is not None:
		window.after_cancel(timer)
	reps = 1
	work_sec = WORK_MIN * 60
	count_down(work_sec)
	my_label.config(text="Working", fg=GREEN)
	work_sessions += 1
 

def start_break_time():
	global reps
	global timer
	global work_sessions
	if timer is not None:
		window.after_cancel(timer)
	reps = 2
	if work_sessions % 4 == 0:
		break_sec = LONG_BREAK_MIN * 60
		my_label.config(text="Long Break", fg=RED)
	else:
		break_sec = SHORT_BREAK_MIN * 60
		my_label.config(text="Short Break", fg=RED)
	count_down(break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
	global marks
	minutes = math.floor(count / 60)
	seconds = count % 60
	if seconds < 10:
		seconds = f"0{seconds}"
	canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
	if count > 0:
		global timer
		timer = window.after(1000, count_down, count - 1)
	else:
		global reps
		if reps == 1:
			start_break_time()
			os.system('play Game-time-sound-effect.mp3 trim 0 2')
		else:
			start_work_time()
			os.system('play Gentle-wake-alarm-clock.mp3 trim 0 2')
		if reps % 2 == 0:
			marks += "✔"
			my_label_1.config(text=marks)
			my_label_1.grid(row=3, column=1)
			# my_label.config(text=f"Work{'✔' * (reps // 2)}", fg=GREEN)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_imp = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_imp)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

my_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW, highlightthickness=0)
my_label.grid(row=0, column=1)

my_label_1 = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)

button_1 = Button(text="Start Work", highlightthickness=0, command=start_work_time)
button_1.grid(row=2, column=0)

button_2 = Button(text="Start Break", highlightthickness=0, command=start_break_time)
button_2.grid(row=2, column=1)

button_3 = Button(text="Reset", highlightthickness=0, command=reset)
button_3.grid(row=2, column=2)

window.mainloop()